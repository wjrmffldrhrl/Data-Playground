# Data Playground

# Prerequisites

## Create Docker Network
```sh
docker network create data-playground
```

# Messaging Queue

## Kafka
```sh
cd message_queue/kafka
docker-compose up --build -d
```

# Producer

## Simple Log generator
```sh
cd producer/simple_log_generator
sh run.sh
```

# Consumer

## Kafka CLI
```sh
cd message_queue/kafka
docker-compose exec kafka1 kafka-console-consumer --bootstrap-server kafka1:19091 kafka2:19092 kafka3:19093  --topic "data-playground"  --from-beginning
```