from datetime import datetime
from models.policy import Policy
from models.endorsement import Endorsement

policies = {}
policy_counter = 0


def create_policy(insurer_first_name, insurer_last_name, lob, address, effective_date):
    global policy_counter
    policy_counter += 1
    policy_id = f"POL{policy_counter}"

    new_policy = Policy(policy_id, insurer_first_name, insurer_last_name, lob, address, effective_date)
    policies[policy_id] = new_policy

    return new_policy


def get_all_policies():
    return list(policies.values())


def get_policy_by_id(policy_id):
    return policies.get(policy_id)


def add_endorsement(policy, data):
    policy.endorsement_counter += 1
    endorsement_id = f"END{policy.endorsement_counter}"

    previous_values = {}
    for field in data:
        previous_values[field] = getattr(policy, field)

    new_endorsement = Endorsement(
        endorsement_id,
        "ENDORSEMENT",
        data,
        previous_values,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    policy.endorsements.append(new_endorsement)

    for field in data:
        setattr(policy, field, data[field])

    return new_endorsement