import uuid

def generate_unique_empID():
    return uuid.uuid4().hex[:6]
