from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092',
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'},
}

p = Producer(conf)
    
def produce_message(message):

    try:
        # Envia a mensagem
        p.produce("meu-topico", value=message, callback=delivery_callback)
        print("Mensagem enviada com sucesso para o tópico meu-topico")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {str(e)}")


def delivery_callback(err, msg):
    if err:
        print('%% Message failed delivery: %s\n', err)
    else:
        print('%% Message delivered to %s [%d]\n',
            (msg.topic(), msg.partition()))
