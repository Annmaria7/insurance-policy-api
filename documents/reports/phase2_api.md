# 📌 Phase 2: API Development – Policy Creation

---

## 🎯 Objective

Build a REST API to create an insurance policy with proper validations based on real-world P&C insurance rules.

---

## 🧱 API Overview

### Endpoint
POST /policy

### Description
This API is used to create a new insurance policy by capturing insurer details, line of business (LOB), and effective date.

---

## 📥 Request Payload

{
  "insurer_first_name": "Ann",
  "insurer_last_name": "Maria",
  "lob": "Auto",
  "effective_date": "2026-03-18"
}

---

## 📌 Field Details

| Field Name           | Description                                      | Mandatory |
|---------------------|--------------------------------------------------|----------|
| insurer_first_name  | First name of the insured person                 | Yes      |
| insurer_last_name   | Last name of the insured person                  | Yes      |
| lob                 | Line of Business (Auto/Health/Property)          | Yes      |
| effective_date      | Policy start date (YYYY-MM-DD)                   | Yes      |

---

## 📤 Success Response

{
  "message": "Policy created successfully",
  "data": {
    "insurer_first_name": "Ann",
    "insurer_last_name": "Maria",
    "lob": "Auto",
    "effective_date": "2026-03-18"
  }
}

---

## ❌ Error Handling & Validations

### 1. Required Field Validation
- All fields must be provided
- Missing values will return an error

Example:
{
  "error": "All fields are required"
}

---

### 2. LOB Validation
- Only the following values are allowed:
  - Auto
  - Health
  - Property

Example:
{
  "error": "Invalid LOB. Allowed: ['Auto', 'Health', 'Property']"
}

---

### 3. Date Format Validation
- Date must follow YYYY-MM-DD format

Example:
{
  "error": "Invalid date format. Use YYYY-MM-DD"
}

---

## 🧪 Testing Approach

API testing was performed using Postman.

### Test Scenarios Covered:
- Valid request (happy path)
- Missing fields
- Invalid LOB values
- Incorrect date format

---

## 🧠 Key Learnings

- Implemented REST API using Flask
- Applied backend validations for data integrity
- Understood importance of domain-specific rules in insurance systems
- Gained hands-on experience in API testing using Postman
- Identified gaps when validation was missing and fixed them

---

## 🔗 Future Enhancements

- Add Policy ID generation
- Store policy data in memory/database
- Implement Policy Endorsement API
- Add Renewal functionality
- Introduce authentication & authorization

---

## 💼 Domain Insight

In Property & Casualty (P&C) Insurance:
- Policy creation is the first step in policy lifecycle
- Policy updates are handled via endorsements, not direct updates
- Data validation is critical for underwriting and compliance