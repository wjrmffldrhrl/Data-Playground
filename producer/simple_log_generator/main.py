import random
import time
from kafka import KafkaProducer
import os
import json
import uuid
from datetime import datetime
from datetime import timedelta
import json

# 프로듀서 생성
producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['kafka1:19091', 'kafka2:19092', 'kafka3:19093'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    )
# 특정 토픽
topic = 'data-playground'

event_names = [
    'clicked',
    'shown',
]

user_ids = [f'{user_id}' for user_id in range(1, 100)]

app_versions = ['1.0.0', '1.0.1', '1.1.0', '2.0.0']

while True:
    
    event_time = datetime.utcnow() + timedelta(seconds=random.randint(-3600, 3600))

    event = {
        'id': f'{uuid.uuid4()}',
        'event_name': random.choice(event_names),
        'event_ts': f'{int(round(event_time.timestamp()))}',
        'user_id': random.choice(user_ids),
        'app_version': random.choice(app_versions),
        'event_time': event_time.strftime('%Y-%m-%d %H:%M:%S'),
    }
    
    event_log = json.dumps(event)

    # 토픽에 메시지 전송
    producer.send(topic, event_log)
    producer.flush()
    print(event_log)
    
    # 1초 대기
    time.sleep(1)
