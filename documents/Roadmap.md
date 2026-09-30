# Roadmap

This project is being built in phases, moving from a local prototype toward a documented, reproducible cloud deployment.

- [x] **Phase 1 — Clean & reorganize**
  Fixed a broken `requirements.txt` (was frozen from the wrong Python environment), secured `.pem` handling in `.gitignore`, and reorganized a single flat `app.py` into a layered `models/ routes/ services/ utils/` structure. Added a Postman collection for repeatable testing. See [architecture.md](./architecture.md).

- [ ] **Phase 2 — Real database**
  Replace the in-memory dictionary in `services/policy_service.py` with PostgreSQL. Expected to be the *only* file that changes, by design — see the layering rationale in [architecture.md](./architecture.md).

- [ ] **Phase 3 — Production-ready Flask**
  Gunicorn instead of Flask's development server, environment variable configuration, structured logging.

- [ ] **Phase 4 — Docker**
  Containerize the app once Phases 2–3 are complete, so the image reflects a production-shaped app rather than a local prototype.

- [ ] **Phase 5 — AWS deployment**
  EC2, VPC, and Security Group configuration. A prior undocumented, un-reproducible deployment attempt is being redone properly this time, captured either in Terraform or in explicit deployment documentation.

- [ ] **Phase 6 — Terraform**
  Infrastructure provisioned as code rather than manual console configuration.

- [ ] **Phase 7 — GitHub Actions**
  CI/CD pipeline: test → build Docker image → deploy.

- [ ] **Phase 8 — CloudWatch monitoring**
  Logs and metrics for the deployed application.