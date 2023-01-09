import random
import time
from kafka import KafkaProducer
import os
import json

# 프로듀서 생성
producer = KafkaProducer(
        acks=0,
        compression_type="gzip",
        bootstrap_servers=["kafka1:19091", "kafka2:19092", "kafka3:19093"],
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    )
# 특정 토픽
topic = 'data-playground'

while True:
    # 랜덤 로그 생성
    log = f'log {random.random()}'
    
    # 토픽에 메시지 전송
    producer.send(topic, log)
    producer.flush()
    print(f'sent message: {log}')
    
    # 1초 대기
    time.sleep(1)