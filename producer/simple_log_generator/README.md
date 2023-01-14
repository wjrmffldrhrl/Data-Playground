# Simple Log Generator
This generator just generating user event log like this

```json
{"id": "734bb8d4-7dd5-4d12-993c-7783a3ff9485", "event_name": "clicked", "event_ts": "1673361675", "user_id": "44", "app_version": "2.0.0", "event_time": "2023-01-10 14:41:14"}

{"id": "969a736e-c978-4fb6-9eff-2cdf065afd15", "event_name": "clicked", "event_ts": "1673362957", "user_id": "48", "app_version": "1.0.0", "event_time": "2023-01-10 15:02:36"}

{"id": "7aa524d4-2997-496e-9cfe-da1ef6f030e0", "event_name": "clicked", "event_ts": "1673362467", "user_id": "16", "app_version": "2.0.0", "event_time": "2023-01-10 14:54:26"}

{"id": "2bbd29b7-b319-446b-819e-20cf4296287a", "event_name": "shown", "event_ts": "1673360022", "user_id": "73", "app_version": "1.0.0", "event_time": "2023-01-10 14:13:41"}

{"id": "ee32b89f-ec7c-48fe-92ea-28174774f673", "event_name": "clicked", "event_ts": "1673362143", "user_id": "59", "app_version": "1.0.1", "event_time": "2023-01-10 14:49:02"}

{"id": "879fe510-523e-4d8a-bea8-a6d241ba65be", "event_name": "clicked", "event_ts": "1673361823", "user_id": "11", "app_version": "1.1.0", "event_time": "2023-01-10 14:43:42"}

{"id": "1a6ab329-0627-4e33-bdf7-d8b2fd287997", "event_name": "clicked", "event_ts": "1673358425", "user_id": "38", "app_version": "2.0.0", "event_time": "2023-01-10 13:47:04"}
```

# How to Run

```sh
cd producer/simple_log_generator
sh run.sh
```