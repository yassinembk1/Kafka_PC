# 🚀 Simple Kafka Producer/Consumer Python Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-KRaft%20Mode-orange?logo=apachekafka)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A minimal **publish–subscribe system** built with **Apache Kafka** (in **KRaft mode**) using **Python** for producing and consuming messages.  
The entire setup runs seamlessly in **Docker Compose**, making it easy to deploy and test locally.

---

## 📂 Project Structure

| File | Description |
|------|--------------|
| 🐍 **producer.py** | Sends random product orders to a Kafka topic. |
| 🧠 **Listner.py** | Listens to the Kafka topic and prints received orders. |
| 🐳 **docker-compose.yml** | Defines the Kafka broker/controller in a single-node setup. |
| 📦 **requirements.txt** | Lists required dependencies (`confluent-kafka`). |

---

## 🛠️ Prerequisites

Make sure you have the following installed:

- 🐋 **Docker** and **Docker Compose**
- 🐍 **Python 3.8+**

---

## ⚙️ 1. Environment Setup

### 🔧 Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

📦 Install Dependencies
pip install -r requirements.txt

🐳 2. Start the Kafka Cluster

Use Docker Compose to launch the Kafka container:

docker compose up -d


Starts Kafka in KRaft mode (broker + controller in one node).

The service is available at localhost:9092.

You can verify the container is running:

docker ps

💻 3. Run the Applications

You’ll need two terminal windows — both with the virtual environment activated.

🧩 A. Start the Consumer (Terminal 1)
python Listner.py


Subscribes to the topic (e.g., orders).

Waits for new messages from Kafka


🚀 B. Start the Producer (Terminal 2)
python producer.py


You’ll see:

Press Enter to create a new order...


Each time you press Enter, a random order (e.g., "Smartphone") is generated and sent to Kafka.

🔁 C. Observe the Data Flow

When the producer sends a message, the consumer instantly receives it:

📦 Received order: Smartphone


✅ Congratulations! You just built a working Kafka Producer–Consumer pipeline in Python.

🛑 4. Cleanup

When finished:

🧹 Stop the Python Scripts

Press Ctrl + C in both terminals.

🐋 Stop the Docker Containers
docker compose down


This will stop the Kafka container and remove associated resources.


💡 Tips & Next Steps

You can extend this project by:

Adding multiple consumers to test Kafka’s load balancing.

Creating custom topics for various data streams.

Implementing JSON serialization/deserialization for structured data.

Using Avro or Protobuf with a Schema Registry.

🧠 Summary

This project provides a simple yet powerful introduction to how Kafka works in a publish/subscribe model with Python clients.
Using Docker Compose makes local experimentation fast and consistent.

👨‍💻 Author

Mohammed Yassine Bakhtaoui