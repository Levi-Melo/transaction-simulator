import os
from dotenv import load_dotenv

absolute_path = os.path.dirname(__file__)
relative_path = "../.env"
dot_env_path = os.path.join(absolute_path, relative_path)

load_dotenv(dot_env_path)

sink_transactions_topic = os.getenv("SINK_TRANSACTIONS_TOPIC")
kafka_broker = os.getenv("KAFKA_BROKER")


