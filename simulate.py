import random
import time

from producer import produce_message
from transaction import create_transaction

def generate_simulated_transactions():
    max_number = random.randint(1, 100)
    users = []
    for _ in range(10):
        users.append(random.randint(0, max_number))

    for user in users:
        produce_message(create_transaction(user))

    time.sleep(random.randint(3, 9))

