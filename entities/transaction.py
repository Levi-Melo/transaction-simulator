import json
import random
from datetime import datetime, timedelta

from entities.coordinate import CoordinateGenerator

# Uso da classe
generator = CoordinateGenerator()

def generate_random_hourly_data(base_date):
    # Define o intervalo de horas para variações
    hour_range = timedelta(hours=24)
    
    # Gera uma hora aleatória dentro do intervalo de 24 horas
    random_hours = base_date + random_timedelta(hour_range)
    
    return random_hours

def random_timedelta(td):
    hours, remainder = divmod(td.total_seconds(), 3600)
    return timedelta(hours=random.uniform(-hours, hours))


def create_transaction(user):
    transaction = {
        "id": f"SIM{random.randint(1000000, 9999999)}",
        "type": random.choice(["purchase", "payment"]),
        "amount": round(random.uniform(10, 100), 2),
        "timestamp": datetime.now().isoformat(),
        "details": json.dumps({
            "product_category": random.choice(["electronics", "clothing", "home_goods"]),
            "product_name": f"Product_{random.randint(1000, 9999)}",
            "quantity": random.randint(1, 5)
        }),
        "user": user,
        "payment_info": {
            "method": random.choice(["credit_card", "debit_card", "bank_transfer"]),
            "currency": random.choice(["USD", "BRL" "EUR"])
        },
        "transaction_status": random.choice(["completed", "pending", "failed"]),
        "merchant_id": f"MERCHANT{random.randint(1000, 9999)}",
        "time_info": datetime.timestamp(generate_random_hourly_data(datetime.now()))
    }
    
    coordinates = generator.get_coordinates_for_user(user)
    
    transaction["geo_info"] = {
        "latitude": round(coordinates[0], 6),
        "longitude": round(coordinates[1], 6)
    }
    
    if random.random() < 0.3:
        transaction["device_info"] = {
            "type": random.choice(["mobile", "desktop", "tablet"]),
            "browser": random.choice(["Chrome", "Firefox", "Safari"])
        }
        transaction["security_info"] = {
            "ip_address": ".".join(map(str, (random.randint(0, 255) for _ in range(4)))),
            "risk_score": round(random.uniform(0, 100), 2)
        }

    return json.dumps(transaction)
