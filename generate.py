import json
from models import User, Device, Transaction
import random, datetime, time, uuid

def insert_user_device(session):
    with open('user_device.json', 'r') as f:
        data=json.loads(f.read())
    for ddata in data:
        try:
            user=User(username=ddata['username'], lokasi=ddata['lokasi'])
            session.add(user)
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        for ddevice in ddata['device']:
            try:
                device=Device(id=ddevice, user_id=user.id)
                session.add(device)
                session.commit()
            except Exception as e:
                print(e)
                session.rollback()

def generate_dummy_data(session, how_many=1000):
    devices=[device.id for device in session.query(Device).all()]
    amount=range(10, 1000)
    start_time=int(time.mktime(datetime.datetime(2019, 1, 1).timetuple()))
    end_time=int(time.mktime(datetime.datetime(2019, 12, 31).timetuple()))
    timetrx=range(start_time, end_time)
    for _ in range(1, how_many+1):
        if _ % 1000 == 0:
            print(f"{_} data has been inserted")
        trx=Transaction(
            id=str(uuid.uuid4()), 
            amount=random.choice(amount), 
            time=random.choice(timetrx), 
            device_id=random.choice(devices)
        )
        session.add(trx)
        session.commit()