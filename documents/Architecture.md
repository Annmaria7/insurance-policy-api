# Architecture

## Layered structure

```
Client (Postman today)
   │
   ▼
routes/          → HTTP request/response handling only (thin)
   │
   ▼
services/        → business logic + storage (in-memory dict, will become DB)
   │
   ▼
models/          → Policy and Endorsement data shapes
   │
utils/           → reusable, framework-agnostic validation rules
```

## Design principle

Every file's responsibility was decided using one test: **"If I swapped Flask for a different framework, would this code have to change?"**

- **routes/** — yes, would change completely. Only place that touches `request` or `jsonify`.
- **services/** — no. Contains policy/endorsement logic and storage access. Never imports anything Flask-specific.
- **models/** — no. Just defines what a Policy and an Endorsement *are* — their fields and sensible defaults (e.g. a new Policy always starts with `endorsements=[]`, `endorsement_counter=0`, so no code anywhere has to defensively check whether those fields exist).
- **utils/** — no. Small, independently reusable rule checks (valid LOB, valid date format, required fields present, allowed endorsement fields) — each usable outside HTTP entirely (e.g. from a CLI tool).

A consequence of this split: **only `services/policy_service.py` will change in Phase 2** when the in-memory dictionary is replaced with a real database. `routes/`, `models/`, and `utils/` are expected to stay untouched.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/policy` | Create a new policy |
| GET | `/policies` | Get all policies |
| GET | `/policy/{policy_id}` | Get a single policy (summary view — endorsements omitted) |
| POST | `/policy/{policy_id}/endorse` | Apply an endorsement to a policy |
| GET | `/policy/{policy_id}/endorsements` | Get full endorsement history for a policy |

**Design decision:** `GET /policy/{policy_id}` deliberately excludes endorsement history, keeping the summary response lean. This is a decision about *this endpoint's response shape*, not about the Policy model — the full data still exists and is available via the dedicated endorsements endpoint. The service layer (`get_policy_by_id`) always returns the full, unshaped object; the route decides what to strip for its specific response.

## Project structure

```
insurance-policy-api/
│
├── app.py                  # entry point — creates the Flask app, wires routes
├── requirements.txt
├── .gitignore
├── insurance-api.postman_collection.json
│
├── documents/               # phase-by-phase design notes (original planning docs)
├── docs/                     # this documentation
│
├── models/
│   ├── policy.py
│   └── endorsement.py
│
├── routes/
│   └── policy_routes.py
│
├── services/
│   └── policy_service.py
│
└── utils/
    └── validators.py
```

## Known limitation

`Policy` and `Endorsement` objects aren't directly JSON-serializable (custom Python objects aren't handled automatically by Flask's `jsonify`). Routes convert them using `vars(obj)`, and any *nested* objects (e.g. `Endorsement` objects inside a `Policy`'s `endorsements` list) must be converted individually — `vars()` only converts one layer deep. This was caught and fixed during development in both `endorse_policy_route` and `get_all_policies_route`.