class Endorsement:
    def __init__(self, endorsement_id, endorsement_type, changes, previous_values, timestamp):
        self.endorsement_id = endorsement_id
        self.endorsement_type = endorsement_type
        self.changes = changes
        self.previous_values = previous_values
        self.timestamp = timestamp