# 📌 Phase 3: Policy Retrieval APIs

---

## 🎯 Objective

Implement APIs to retrieve stored insurance policies using in-memory storage.

---

## 🧱 API Overview

This phase introduces retrieval capabilities for policies created in the system.

---

## 🔍 API 1: Get All Policies

### Endpoint
GET /policies

### Description
Fetches all policies stored in the system.

---

### 📤 Success Response

{
  "policies": [
    {
      "policy_id": "POL1001",
      "insurer_first_name": "Ann",
      "insurer_last_name": "Maria",
      "lob": "Auto",
      "effective_date": "2026-03-18"
    },
    {
      "policy_id": "POL1002",
      "insurer_first_name": "John",
      "insurer_last_name": "Doe",
      "lob": "Health",
      "effective_date": "2026-04-01"
    }
  ]
}

---

## 🔍 API 2: Get Policy by ID

### Endpoint
GET /policy/{policy_id}

### Description
Fetches a specific policy using its unique Policy ID.

---

### ✅ Example Request
GET /policy/POL1001

---

### 📤 Success Response

{
  "policy_id": "POL1001",
  "insurer_first_name": "Ann",
  "insurer_last_name": "Maria",
  "lob": "Auto",
  "effective_date": "2026-03-18"
}

---

### ❌ Error Response (Policy Not Found)

{
  "error": "Policy not found"
}

---

## 🧠 Implementation Details

- Policies are stored in an in-memory dictionary
- Policy ID is used as the key for efficient lookup
- Retrieval is performed using direct dictionary access

---

## 🧪 Testing Approach

API testing was performed using Postman.

### Test Scenarios Covered:

- Fetch all policies after multiple creations
- Fetch a valid policy by ID
- Fetch a non-existing policy ID
- Verify correct error handling (404 response)

---

## ⚠️ Limitations

- Data is stored in-memory and will be lost if the server restarts
- No database persistence implemented yet

---

## 🧠 Key Learnings

- Implemented GET APIs for data retrieval
- Used path parameters to fetch specific resources
- Understood importance of efficient data structures (dictionary)
- Applied error handling for invalid resource access

---

## 🔗 Future Enhancements

- Add database integration for persistent storage
- Implement filtering (e.g., by LOB, date)
- Add pagination for large datasets