import json
from datetime import datetime
import random

def create_transaction(user):
    return json.dumps({
        "id": f"SIM{random.randint(1000000, 9999999)}",
        "type": random.choice(["purchase", "payment"]),
        "amount": round(random.uniform(10, 100), 2),
        "timestamp": datetime.now().isoformat(),
        "details": json.dumps({"product": random.choice(["A", "B", "C"])}),
        "user": user
    })    