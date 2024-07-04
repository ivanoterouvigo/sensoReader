# sensoReader
lector de datos sensor

# architecture

sensor_app/
├── main.py

├── sensor.py

├── database.py

├── nats_client.py

└── config.py


# needed libraries
pip install nats-py
pip install sqlite3 

# to run the app

python main.py --sensor_type mockup --interval 5 --range_min 100 --range_max 50000 --db_uri "sensor_data.db"
