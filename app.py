from flask import Flask, request, jsonify
from datetime import datetime
policies = {}
policy_counter = 1000

app = Flask(__name__)

@app.route("/")
def home():
    return "Insurance Policy API is running 🚀"


@app.route("/policy", methods=["POST"])
def create_policy():
    data = request.get_json()

    insurer_first_name = data.get("insurer_first_name")
    insurer_last_name = data.get("insurer_last_name")
    lob = data.get("lob")
    effective_date = data.get("effective_date")

    # ✅ Validation 1: Required fields
    if not insurer_first_name or not insurer_last_name or not lob or not effective_date:
        return jsonify({
            "error": "All fields are required"
        }), 400

    # ✅ Validation 2: LOB check
    valid_lobs = ["Auto", "Health", "Property"]
    if lob not in valid_lobs:
        return jsonify({
            "error": f"Invalid LOB. Allowed: {valid_lobs}"
        }), 400

    # ✅ Validation 3: Date format check
    try:
        datetime.strptime(effective_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({
            "error": "Invalid date format. Use YYYY-MM-DD"
        }), 400

    global policy_counter

    policy_counter += 1
    policy_id = f"POL{policy_counter}"

    policy_data = {
    "policy_id": policy_id,
    "insurer_first_name": insurer_first_name,
    "insurer_last_name": insurer_last_name,
    "lob": lob,
    "effective_date": effective_date
    }

    policies[policy_id] = policy_data

    print(policy_data)

    return jsonify({"message": "Policy created successfully",
    "data": policy_data
    }), 201

@app.route("/policies", methods=["GET"])
def get_all_policies():
    return jsonify({
        "policies": list(policies.values())
    }), 200

@app.route("/policy/<policy_id>", methods=["GET"])
def get_policy(policy_id):
    policy = policies.get(policy_id)

    if not policy:
        return jsonify({
            "error": "Policy not found"
        }), 404

    policy_copy = policy.copy()
    policy_copy.pop("endorsements", None)
    policy_copy.pop("endorsement_counter", None)

    return jsonify(policy_copy), 200

@app.route("/policy/<policy_id>/endorse", methods=["POST"])
def endorse_policy(policy_id):
    data = request.get_json()

    # Step 1: Check if policy exists
    policy = policies.get(policy_id)
    if not policy:
        return jsonify({
            "error": "Policy not found"
        }), 404

    # Step 2: Define allowed fields
    allowed_fields = ["address", "effective_date"]

    # Step 3: Validate fields
    for field in data.keys():
        if field not in allowed_fields:
            return jsonify({
                "error": f"{field} cannot be changed via endorsement"
            }), 400

    # Step 4: Initialize endorsement tracking
    if "endorsements" not in policy:
        policy["endorsements"] = []

    if "endorsement_counter" not in policy:
        policy["endorsement_counter"] = 0

    # Step 5: Generate endorsement ID (per policy)
    policy["endorsement_counter"] += 1
    endorsement_id = f"END{policy['endorsement_counter']}"

    # Step 6: Create endorsement record
    endorsement_record = {
        "endorsement_id": endorsement_id,
        "type": "ENDORSEMENT",
        "changes": data,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Step 7: Store endorsement history
    policy["endorsements"].append(endorsement_record)

    # Step 8: Apply updates to policy
    for field in data:
        policy[field] = data[field]

    # Step 9: Return response
    return jsonify({
        "message": "Policy endorsed successfully",
        "endorsement_id": endorsement_id,
        "data": policy
    }), 200

@app.route("/policy/<policy_id>/endorsements", methods=["GET"])
def get_endorsements(policy_id):
    policy = policies.get(policy_id)

    if not policy:
        return jsonify({
            "error": "Policy not found"
        }), 404

    return jsonify({
        "policy_id": policy_id,
        "endorsements": policy.get("endorsements", [])
    }), 200
    
if __name__ == "__main__":
    app.run(debug=True)