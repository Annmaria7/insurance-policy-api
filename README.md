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

Currently running locally with an in-memory store — see [`Roadmap.md`](../Roadmap.md) for the path to the architecture above.

## ⚙️ Tech Stack

**Current:** Python 3.11, Flask 3.1, REST API, Postman
**Planned:** PostgreSQL, Docker, AWS (EC2 / VPC / RDS), Terraform, GitHub Actions, CloudWatch

## 📚 Documentation

- [`Getting-started.md`](../Getting-started.md) — setup and running locally
- [`Architecture.md`](../Architecture.md) — layered structure, API endpoints, design decisions
- [`Testing.md`](../Testing.md) — Postman collection usage
- [`Troubleshooting.md`](../Troubleshooting.md) — common issues
- [`Roadmap.md`](../Roadmap.md) — phased plan from local prototype to AWS deployment

## 👩‍💻 Author

**Ann Maria Anto**
