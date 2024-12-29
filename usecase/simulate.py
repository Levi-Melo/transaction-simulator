import random
import time

from infra.producer import produce_message
from entities.transaction import create_transaction

def simulated_transactions():
    max_number = random.randint(1, 15)
    users = []
    for _ in range(10):
        users.append(random.randint(0, max_number))

    for user in users:
        produce_message(create_transaction(user).encode('utf-8'))

    time.sleep(0.5)

