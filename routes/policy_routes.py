from flask import request, jsonify

from services.policy_service import (
    create_policy,
    get_all_policies,
    get_policy_by_id,
    add_endorsement,
)
from utils.validators import (
    has_missing_fields,
    is_valid_lob,
    is_valid_date,
    get_disallowed_field,
)


def register_routes(app):

    @app.route("/policy", methods=["POST"])
    def create_policy_route():
        data = request.get_json()

        insurer_first_name = data.get("insurer_first_name")
        insurer_last_name = data.get("insurer_last_name")
        lob = data.get("lob")
        address = data.get("address")
        effective_date = data.get("effective_date")

        if has_missing_fields([insurer_first_name, insurer_last_name, lob, address, effective_date]):
            return jsonify({"error": "All fields are required"}), 400

        if not is_valid_lob(lob):
            return jsonify({"error": "Invalid LOB. Allowed: Auto, Health, Property"}), 400

        if not is_valid_date(effective_date):
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        new_policy = create_policy(insurer_first_name, insurer_last_name, lob, address, effective_date)

        return jsonify({
            "message": "Policy created successfully",
            "data": vars(new_policy)
        }), 201

    @app.route("/policies", methods=["GET"])
    def get_all_policies_route():
        all_policies = get_all_policies()

        policies_data = []
        for p in all_policies:
            p_data = vars(p).copy()
            p_data["endorsements"] = [vars(e) for e in p.endorsements]
            policies_data.append(p_data)

        return jsonify({"policies": policies_data}), 200

    @app.route("/policy/<policy_id>", methods=["GET"])
    def get_policy_route(policy_id):
        policy = get_policy_by_id(policy_id)

        if not policy:
            return jsonify({"error": "Policy not found"}), 404

        policy_data = vars(policy).copy()
        policy_data.pop("endorsements", None)
        policy_data.pop("endorsement_counter", None)

        return jsonify(policy_data), 200

    @app.route("/policy/<policy_id>/endorse", methods=["POST"])
    def endorse_policy_route(policy_id):
        data = request.get_json()

        policy = get_policy_by_id(policy_id)
        if not policy:
            return jsonify({"error": "Policy not found"}), 404

        bad_field = get_disallowed_field(data)
        if bad_field:
            return jsonify({"error": f"{bad_field} cannot be changed via endorsement"}), 400

        new_endorsement = add_endorsement(policy, data)

        policy_data = vars(policy).copy()
        policy_data["endorsements"] = [vars(e) for e in policy.endorsements]

        return jsonify({
            "message": "Policy endorsed successfully",
            "endorsement_id": new_endorsement.endorsement_id,
            "data": policy_data
        }), 200

    @app.route("/policy/<policy_id>/endorsements", methods=["GET"])
    def get_endorsements_route(policy_id):
        policy = get_policy_by_id(policy_id)

        if not policy:
            return jsonify({"error": "Policy not found"}), 404

        return jsonify({
            "policy_id": policy_id,
            "endorsements": [vars(e) for e in policy.endorsements]
        }), 200