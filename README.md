<div align="center">

# 🚀 **Simple Kafka Producer/Consumer Python Project**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-KRaft%20Mode-orange?logo=apachekafka)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

<p align="center">
A **minimal** and **hands-on** publish–subscribe system built with ⚙️ <b>Apache Kafka</b> (KRaft mode) using <b>Python</b> clients — all running smoothly inside <b>Docker Compose</b> 🐋.
</p>

---

## 🏗️ Project Overview

This project demonstrates the **producer–consumer** model with Kafka:  
One script produces random product orders, and another consumes them in real-time.

---

## 📂 Folder Structure

| 🗃️ File | 🧩 Description |
|------|--------------|
| 🐍 **producer.py** | Generates and sends random product orders to Kafka. |
| 🧠 **Listner.py** | Consumes messages from the Kafka topic and prints them in real-time. |
| 🐳 **docker-compose.yml** | Single-node Kafka setup (broker + controller with KRaft mode). |
| 📦 **requirements.txt** | Python dependencies (`confluent-kafka`). |

---

## ⚙️ Prerequisites

Before running, ensure you have:

- 🐋 **Docker** & **Docker Compose**
- 🐍 **Python 3.8+**

> 💡 Tip: Check your installations with `docker --version` and `python --version`.

---

## 🧩 Step 1 — Environment Setup

### 🔹 Create & Activate a Virtual Environment
```bash
python3 -m venv venv
# Activate on macOS/Linux
source venv/bin/activate
# Activate on Windows
venv\Scripts\activate
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🐳 Step 2 — Start the Kafka Cluster

Launch Kafka with Docker Compose:

```bash
docker compose up -d
```

✅ **Kafka is ready!**  
Runs in **KRaft mode** (broker + controller in one node).  
Accessible on **localhost:9092**.

Check the container status:
```bash
docker ps
```

---

## 💻 Step 3 — Run the Project

You’ll need **two terminals** (both with the virtual environment activated).

### 🧠 Terminal 1: Start the Consumer
```bash
python Listner.py
```

🟢 Waits for messages from Kafka.

### ⚡ Terminal 2: Start the Producer
```bash
python producer.py
```

You’ll see:
```
Press Enter to create a new order...
```

Each time you press **Enter**, a random order (e.g. _“Smartphone”_) gets published to Kafka.  
Meanwhile, the consumer will instantly print:

```
📦 Received order: Smartphone
```

---

## 🧹 Step 4 — Cleanup

### 🔸 Stop the Scripts
Press **Ctrl + C** in both terminals.

### 🔸 Shutdown Kafka
```bash
docker compose down
```

This will stop and remove all Kafka containers and volumes.

---

## 🌱 Next Steps & Ideas

Want to power this up? Here are some ideas:
- ⚖️ Add multiple consumers to test Kafka load-balancing.
- 🧾 Use JSON serialization for rich, structured messages.
- 🧩 Experiment with Avro/Protobuf + Schema Registry.
- 🧠 Integrate monitoring tools like Kafdrop or Prometheus.

---

## 🧠 Summary

🔥 You’ve built a fully working **Kafka Producer–Consumer** pipeline in Python!  
Using **Docker Compose** makes running and testing fast, isolated, and repeatable.  
This setup gives you a solid foundation for learning **event-driven architectures** and real-time data streaming.

---

<div align="center">

👨‍💻 **Author:** [Mohammed Yassine Bakhtaoui](#)  
🪪 **License:** MIT  
💙 *Made with Python, Kafka, and 🚀 enthusiasm!*

</div>