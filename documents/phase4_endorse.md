# 📌 Phase 4: Policy Endorsement API

---

## 🎯 Objective

Implement a domain-aligned Policy Endorsement API to allow controlled updates to policy attributes while maintaining an audit trail of all changes.

---

## 🧠 Domain Understanding

In Property & Casualty (P&C) insurance systems:

- Policies are NOT directly modified after creation
- Changes are applied via **endorsements**
- Endorsements are mid-term transactions that:
  - Update specific allowed fields
  - Maintain history for audit and traceability

---

## ⚠️ Key Domain Rules

### ❌ Non-Endorsable Fields
The following fields cannot be changed via endorsement:

- Line of Business (LOB)
- Core policy structure

These require creation of a new policy instead.

---

### ✅ Endorsable Fields

For this implementation, the following fields are allowed:

- address
- effective_date

---

## 🧱 Data Model Enhancement

Each policy is enhanced with endorsement tracking:

- endorsements → stores history of all changes
- endorsement_counter → generates unique endorsement IDs per policy

---

### 📦 Policy Structure

{
  "policy_id": "POL1001",
  "insurer_first_name": "Ann",
  "insurer_last_name": "Maria",
  "lob": "Auto",
  "effective_date": "2026-03-18",
  "address": "Kochi",
  "endorsements": [],
  "endorsement_counter": 0
}

---

## 🔢 Endorsement ID Design

- Endorsement IDs are generated per policy
- Format: END1, END2, ...
- Not globally unique
- Scoped within each policy

---

## 🔄 API Design

### Endpoint
POST /policy/{policy_id}/endorse

---

## 📥 Request Payload

{
  "address": "Kochi, Kerala",
  "effective_date": "2026-04-01"
}

---

## 🔄 Workflow

1. Validate if policy exists
2. Validate request fields against allowed list
3. Generate endorsement ID (per policy)
4. Create endorsement record with timestamp
5. Store endorsement in policy history
6. Apply updates to policy
7. Return updated policy

---

## 📤 Success Response

{
  "message": "Policy endorsed successfully",
  "endorsement_id": "END1",
  "data": {
    "policy_id": "POL1001",
    "insurer_first_name": "Ann",
    "insurer_last_name": "Maria",
    "lob": "Auto",
    "effective_date": "2026-04-01",
    "address": "Kochi, Kerala"
  }
}

---

## 📜 Endorsement History Structure

Each endorsement is stored as:

{
  "endorsement_id": "END1",
  "type": "ENDORSEMENT",
  "changes": {
    "address": "Kochi, Kerala",
    "effective_date": "2026-04-01"
  },
  "timestamp": "2026-03-26 21:00:00"
}

---

## 🔍 Additional API: Get Endorsement History

### Endpoint
GET /policy/{policy_id}/endorsements

---

### 📤 Response

{
  "policy_id": "POL1001",
  "endorsements": [
    {
      "endorsement_id": "END1",
      "type": "ENDORSEMENT",
      "changes": {
        "address": "Kochi, Kerala"
      },
      "timestamp": "2026-03-26 21:00:00"
    }
  ]
}

---

## ⚠️ Error Handling

### Policy Not Found

{
  "error": "Policy not found"
}

---

### Invalid Field Update

{
  "error": "lob cannot be changed via endorsement"
}

---

## 🧪 Testing Approach

API testing was performed using Postman.

### Test Scenarios Covered:

- Valid endorsement with allowed fields
- Multiple endorsements on same policy
- Invalid field updates (e.g., LOB)
- Endorsement on non-existing policy
- Retrieval of endorsement history

---

## 🧠 Key Learnings

- Implemented domain-driven API design
- Applied controlled update logic using endorsements
- Introduced per-policy endorsement ID generation
- Built audit trail using endorsement history
- Separated current state and historical data retrieval

---

## 🔗 Future Enhancements

- Add endorsement version comparison
- Implement rollback functionality
- Introduce database persistence
- Add authentication and authorization
- Deploy application on AWS