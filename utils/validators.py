from datetime import datetime

def has_missing_fields(values):
    for value in values:
        if not value:
            return True
    return False


def is_valid_lob(lob):
    valid_lobs = ["Auto", "Health", "Property"]
    if lob not in valid_lobs:
        return False
    return True


def is_valid_date(effective_date):
    try:
        datetime.strptime(effective_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_disallowed_field(data):
    allowed_fields = ["address", "effective_date"]
    for field in data.keys():
        if field not in allowed_fields:
            return field
    return None