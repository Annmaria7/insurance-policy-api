# 🚀 Insurance Policy API

A backend REST API simulating real-world Property & Casualty (P&C) insurance policy lifecycle operations, including policy creation, retrieval, and endorsements with audit tracking.

---

## 📌 Project Overview

This project demonstrates a domain-driven approach to building insurance systems by implementing:

* Policy creation
* Policy retrieval
* Policy endorsement (mid-term updates)
* Endorsement tracking with audit history

The design follows real-world insurance constraints such as controlled updates and transaction-based modifications.

---

## 🧠 Key Features

### ✅ Policy Management

* Create new insurance policies
* Store policy details using structured data

### 🔍 Policy Retrieval

* Fetch policy details using Policy ID
* Optimized response (excludes heavy historical data)

### 🔄 Policy Endorsement

* Perform controlled updates using endorsements
* Restrict non-editable fields (e.g., LOB)
* Support multiple endorsements per policy

### 🧾 Audit Trail

* Track all endorsements with:

  * Endorsement ID (per policy)
  * Timestamp
  * Changed fields

### 📊 Separation of Concerns

* Separate API for retrieving endorsement history

---

## 🏗️ Project Structure

```
insurance-policy-api/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── documents/
│   ├── phase1_design.md
│   ├── phase2_api.md
│   ├── phase3_retrieval.md
│   ├── phase4_endorse.md
│
├── models/
├── routes/
├── services/
├── utils/
```

---

## ⚙️ Tech Stack

* Python
* Flask
* REST API
* Postman (for testing)

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```
git clone https://github.com/Annmaria7/insurance-policy-api.git
cd insurance-policy-api
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

---

### 3️⃣ Activate environment

**Windows:**

```
venv\Scripts\activate
```

---

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 5️⃣ Run the application

```
python app.py
```

---

### 6️⃣ Access API

```
http://127.0.0.1:5000
```

---

## 🔗 API Endpoints

### 📌 Create Policy

```
POST /policy
```

---

### 📌 Get Policy

```
GET /policy/{policy_id}
```

---

### 📌 Endorse Policy

```
POST /policy/{policy_id}/endorse
```

---

### 📌 Get Endorsement History

```
GET /policy/{policy_id}/endorsements
```

---

## 🧪 Testing

* APIs tested using Postman
* Covers:

  * Valid requests
  * Invalid inputs
  * Edge cases

---

## 🧠 Key Learnings

* Domain-driven API design
* Insurance lifecycle modeling
* Controlled updates using endorsements
* Audit trail implementation
* REST API best practices

---

## 🔮 Future Enhancements

* ## 🔮 Future Enhancements

- Policy Renewal (new term creation)
- Policy Cancellation (terminate active policy)
- Database integration (PostgreSQL / DynamoDB)
- Authentication & authorization
- AWS deployment
- API documentation with Swagger
- Modular architecture (services, routes, models)

---

## 💼 Why this project?

This project goes beyond basic CRUD operations and demonstrates:

* Real-world insurance domain understanding
* Clean API design
* Scalable backend thinking

---

## 👩‍💻 Author

**Ann Maria Anto**

---
