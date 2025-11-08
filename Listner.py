from confluent_kafka import Consumer
import json

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-listeners',
    'auto.offset.reset': 'earliest'
} 

consumer = Consumer(consumer_config)
consumer.subscribe(['orders'])

print("Listening for messages on 'orders' topic...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        val = msg.value().decode('utf-8')
        order = json.loads(val)
        print(f"📦 Received order: {order['item']}")
        
except KeyboardInterrupt:
    print("Shutting down gracefully...")
    pass
finally:
    consumer.close()
    
    
    


