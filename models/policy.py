class Policy:
    def __init__(self, policy_id, insurer_first_name, insurer_last_name, lob, address, effective_date):
        self.policy_id = policy_id
        self.insurer_first_name = insurer_first_name
        self.insurer_last_name = insurer_last_name
        self.lob = lob
        self.address = address
        self.effective_date = effective_date
        self.endorsements = []
        self.endorsement_counter = 0