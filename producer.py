import json
import uuid
from confluent_kafka import Producer 

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}

p = Producer(producer_config)

items = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 'Camera', 'Printer', 'Monitor', 'Keyboard', 'Mouse']

def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered {msg.value().decode('utf-8')} to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
    


try:
    while True:
        input("Press Enter to create a new order...")
        i = uuid.uuid4().int % len(items)
        print(f"📦 Creating order for {items[i]}" )
        order = {
        'order_id': str(uuid.uuid4()),
        'customer_id': str(uuid.uuid4()),
        'item': items[i],
        'amount': 250.75,
        'quantity': 1
    }
        val = json.dumps(order).encode('utf-8')
        p.produce(
        topic= "orders",
        value=val,
        callback=delivery_report
        )
except KeyboardInterrupt:
    print("Shutting down gracefully...")
finally:
    p.flush()






















