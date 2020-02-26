from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base=declarative_base()

class User(Base):
    __tablename__='user'

    # table's columns
    id=Column('id', Integer, primary_key=True)
    username=Column('name', String)
    lokasi=Column('lokasi', String)
    device=relationship('Device', backref='user', lazy=True)

    def __repr__(self):
        return f"{self.username}\t{self.lokasi}"

class Device(Base):
    __tablename__='device'
    
    # table's columns
    id=Column('id', String, primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'))
    trx=relationship('Transaction', backref='device', lazy=True)

    def __repr__(self):
        return f"{self.id}\t{self.user_id}"

class Transaction(Base):
    __tablename__='trx'

    # table's columns
    id=Column('id', String, primary_key=True)
    amount=Column('amount', Integer)
    time=Column('time', Integer)
    device_id=Column(String, ForeignKey('device.id'))

    # create index in time attribute
    __table_args__ = (Index('trx_time_idx', 'time'), )

    def __repr__(self):
        return f"{self.id}\t{self.device_id}\t{self.device.user.username}\t{self.device.user.lokasi}\t{self.amount}\t{self.time}"