# 📌 Phase 1: Research & System Design

---

## 🎯 Objective

Understand the insurance domain and design a basic system workflow for policy management before implementation.

---

## 🧠 Domain Understanding

This project is based on Property & Casualty (P&C) insurance systems.

### Key Concepts:

- A policy represents a contract between insurer and customer
- Policies are created with an effective date
- Each policy belongs to a Line of Business (LOB), such as:
  - Auto
  - Health
  - Property

---

## 🔄 Policy Lifecycle Overview

A typical insurance policy goes through the following stages:

1. Policy Creation (New Business)
2. Policy Endorsement (Updates/Changes)
3. Renewal
4. Cancellation
5. Reinstatement

---

## 🧱 System Design Overview

The system is designed as a REST API-based backend application.

### Core Components:

- API Layer (Flask)
- Business Logic Layer
- Data Storage (In-memory for initial phase)

---

## 🧾 Data Model Design

Each policy contains the following attributes:

- policy_id (system generated)
- insurer_first_name
- insurer_last_name
- lob (Line of Business)
- effective_date

---

## 🔁 Workflow Design

### Policy Creation Flow:

1. User sends request with policy details
2. System validates input data
3. Policy ID is generated
4. Policy is stored in memory
5. Response is returned to user

---

## 🧪 Testing Strategy

The APIs will be tested using Postman.

### Testing Focus Areas:

- Functional validation
- Input validation
- Error handling
- API response verification

---

## 🧠 Design Decisions

### Why In-Memory Storage?

- Simpler implementation for initial phase
- Helps focus on API logic and flow
- Will be replaced with database in future phases

---

## ⚠️ Assumptions

- Only basic policy fields are considered
- No authentication or authorization implemented
- No database persistence in initial phase

---

## 🔗 Future Scope

- Deploy application on AWS as part of final phase after completing core API functionalities
- Implement full policy lifecycle (renewal, cancellation)
- Add authentication and security
- Add database integration

## Note

While the system design includes full policy lifecycle operations such as renewal and cancellation, the current implementation focuses on core functionalities including policy creation, retrieval, and endorsement.

Renewal and cancellation are planned for future phases.
---

## 🧠 Key Learnings

- Understood insurance policy lifecycle
- Designed API workflow before implementation
- Identified key data fields and system components
- Planned structured development using phased approach