# 🚀 Insurance Policy API

A backend REST API simulating real-world Property & Casualty (P&C) insurance policy lifecycle operations — policy creation, retrieval, and endorsements with full audit tracking.

## 🏗️ Target Architecture

```
                    Internet
                       │
                       ▼
                AWS EC2 Instance
                       │
                 Flask REST API
                       │
              ┌────────┴────────┐
              │                 │
             RDS            CloudWatch
          PostgreSQL          Logs/Metrics
```

Currently running locally with an in-memory store — see [`documents/roadmap.md`](./documents/roadmap.md) for the path to the architecture above.

## ⚙️ Tech Stack

**Current:** Python 3.11, Flask 3.1, REST API, Postman
**Planned:** PostgreSQL, Docker, AWS (EC2 / VPC / RDS), Terraform, GitHub Actions, CloudWatch

## 📚 Documentation

- [`documents/getting-started.md`](./documents/getting-started.md) — setup and running locally
- [`documents/architecture.md`](./documents/architecture.md) — layered structure, API endpoints, design decisions
- [`documents/testing.md`](./documents/testing.md) — Postman collection usage
- [`documents/troubleshooting.md`](./documents/troubleshooting.md) — common issues
- [`documents/roadmap.md`](./documents/roadmap.md) — phased plan from local prototype to AWS deployment

## 👩‍💻 Author

**Ann Maria Anto**