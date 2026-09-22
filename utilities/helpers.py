import uuid

def generate_unique_empID():
    return uuid.uuid4().hex[:6]

def generate_unique_first_name():
    return uuid.uuid4().hex[:6]
