from confluent_kafka import Producer
from config.config import sink_transactions_topic,kafka_broker

conf = {
    'bootstrap.servers': kafka_broker,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'},
}

p = Producer(conf)
    
def produce_message(message):
    try:
        # Envia a mensagem
        p.produce(sink_transactions_topic, value=message, callback=delivery_callback)
        print(f"Mensagem enviada com sucesso para o tópico: {sink_transactions_topic}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {str(e)}")


def delivery_callback(err, msg):
    if err:
        print('%% Message failed delivery: %s\n', err)
    else:
        print('%% Message delivered to %s [%d]\n',
            (msg.topic(), msg.partition()))
