# Troubleshooting

### "Policy not found" after previously creating one
Data is stored in memory only. Any app restart — including Flask's debug-mode auto-reload whenever a file is saved — clears all policies. Create a fresh policy via `POST /policy` and update your Postman `policy_id` variable to the new ID.

### `ModuleNotFoundError: No module named 'flask'`
Your virtual environment isn't activated, or dependencies were installed somewhere else. Run:
```
venv\Scripts\activate
pip install -r requirements.txt
```
Confirm Flask is actually present with `pip list` while the venv is active.

### Import errors on startup (`ModuleNotFoundError` for `models`, `routes`, `services`, or `utils`)
Run `python app.py` from the project's root folder — not from inside a subfolder. Also confirm each of `models/`, `routes/`, `services/`, and `utils/` contains an `__init__.py` file (can be empty), which is required for Python to treat them as importable packages.

### `TypeError: Object of type Endorsement is not JSON serializable` (or `Policy`)
`jsonify()` can't serialize custom Python objects directly. `vars(obj)` converts an object to a dict one layer deep — if that object contains a *nested* custom object (e.g. a `Policy`'s `endorsements` list containing `Endorsement` objects), those nested objects must be converted individually before the outer dict is passed to `jsonify`. See [Architecture.md](./Architecture.md#known-limitation) for the pattern used to fix this.

### `requirements.txt` seems to install unrelated packages, or is missing Flask
`requirements.txt` is a snapshot of whichever Python environment was active when `pip freeze` was run — not a definition of what the app needs. If it looks wrong, activate the actual venv the app runs in and compare against `pip list`, then regenerate with `pip freeze > requirements.txt` from that environment.
