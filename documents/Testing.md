# Testing

APIs are tested manually using Postman. A ready-to-import collection covering all five endpoints is included in the repo root: [`Insurance Policy Api.postman_collection.json`](../Insurance Policy API.postman_collection.json).

## Using the collection

1. Import the collection into Postman (File → Import → select the JSON file)
2. Run **Create Policy** first — this generates a policy in the in-memory store and returns a `policy_id`
3. Open the collection's **Variables** tab and set `policy_id` to the value just returned
4. Run the remaining requests — they all reference `{{policy_id}}`, so no further editing is needed

## Requests included

| Request | Method | Purpose |
|---|---|---|
| Create Policy | POST | Creates a policy |
| Get Policy by ID | GET | Fetches one policy (summary view) |
| Get all Policies | GET | Fetches every policy currently in memory |
| Endorse Policy | POST | Applies an endorsement (only `address` and `effective_date` are allowed) |
| Get Endorsements | GET | Fetches full endorsement history for a policy |

## Cases worth testing manually
- Valid creation
- Missing required fields → `400`
- Invalid LOB (not Auto/Health/Property) → `400`
- Invalid date format → `400`
- Endorsing a disallowed field (e.g. `lob`) → `400`
- Fetching a policy/endorsement that doesn't exist → `404`

## Note on the in-memory store
Because data lives only in memory, **restarting the server clears everything** — including after Flask's debug-mode auto-reload on file save. If a saved request suddenly returns "Policy not found," re-run **Create Policy** and update the `policy_id` variable. See [troubleshooting.md](./troubleshooting.md).

## Planned
Automated testing (beyond manual Postman runs) is not yet in place — this is expected to be introduced alongside CI/CD in a later roadmap phase.
