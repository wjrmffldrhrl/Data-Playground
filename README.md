# Data Playground

# Prerequisites
```sh
docker network create data-playground
```

# Kafka
```sh
docker-compose up --build -d
```

# Producer
```sh
docker build -t producer .
sh run.sh
```

# Consumer
```sh
docker-compose exec kafka1 kafka-console-consumer --bootstrap-server kafka1:19091 kafka2:19092 kafka3:19093  --topic "data-playground"  --from-beginning
```