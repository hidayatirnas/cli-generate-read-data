from sqlalchemy import func
from models import Transaction, Device, User
from prettytable import PrettyTable

Map={
    'device_id':Transaction.device_id,
    'username':User.username,
    'lokasi':User.lokasi,
    'timerange':Transaction.time
}

def read_100(session, asc=True):
    if asc:
        data=session.query(Transaction).order_by('time').all()[:100]
    else:
        data=session.query(Transaction).order_by('time').all()[:-101:-1]
    return data

def read_by_filter(session, filter_by, filter_value):
    data=session.query(Transaction).join(Device).join(User).filter(Map[filter_by]==filter_value).all()[:100]
    return data

def read_specific_row(session, row_number):
    data=session.query(Transaction)[row_number]
    return data

def read_max(session, group_by='all'):
    if group_by=='all':
        result=session.query(func.max(Transaction.amount)).scalar()
    elif group_by in ['device_id', 'username', 'lokasi']:
        result=session.query(Map[group_by], func.max(Transaction.amount)).\
            join(Device, Device.id==Transaction.device_id).\
            join(User, Device.user_id==User.id).\
            group_by(Map[group_by]).all()
    else:
        raise ValueError("group_by value should be in between ('all', 'device_id', 'username', 'lokasi')")
    return result

def read_min(session, group_by='all'):
    if group_by=='all':
        result=session.query(func.min(Transaction.amount)).scalar()
    elif group_by in ['device_id', 'username', 'lokasi']:
        result=session.query(Map[group_by], func.min(Transaction.amount)).\
            join(Device, Device.id==Transaction.device_id).\
            join(User, Device.user_id==User.id).\
            group_by(Map[group_by]).all()
    else:
        raise ValueError("group_by value should be in between ('all', 'device_id', 'username', 'lokasi')")
    return result

def read_avg(session, group_by='all'):
    if group_by=='all':
        result=session.query(func.avg(Transaction.amount)).scalar()
    elif group_by in ['device_id', 'username', 'lokasi']:
        result=session.query(Map[group_by], func.avg(Transaction.amount)).\
            join(Device, Device.id==Transaction.device_id).\
            join(User, Device.user_id==User.id).\
            group_by(Map[group_by]).all()
    else:
        raise ValueError("group_by value should be in between ('all', 'device_id', 'username', 'lokasi')")
    return result

def read_sum(session, group_by='all'):
    if group_by=='all':
        result=session.query(func.sum(Transaction.amount)).scalar()
    elif group_by in ['device_id', 'username', 'lokasi']:
        result=session.query(Map[group_by], func.sum(Transaction.amount)).\
            join(Device, Device.id==Transaction.device_id).\
            join(User, Device.user_id==User.id).\
            group_by(Map[group_by]).all()
    else:
        raise ValueError("group_by value should be in between ('all', 'device_id', 'username', 'lokasi')")
    return result

def read_count(session, group_by='all'):
    if group_by=='all':
        result=session.query(func.count(Transaction.amount)).scalar()
    elif group_by in ['device_id', 'username', 'lokasi']:
        result=session.query(Map[group_by], func.count(Transaction.amount)).\
            join(Device, Device.id==Transaction.device_id).\
            join(User, Device.user_id==User.id).\
            group_by(Map[group_by]).all()
    else:
        raise ValueError("group_by value should be in between ('all', 'device_id', 'username', 'lokasi')")
    return result

def split_string_by_tab(string: str):
    splitted=string.split('\t')
    return splitted

def print_table(data, columns: list):
    table=PrettyTable(columns)
    if isinstance(data, list):
        for ddata in data:
            table.add_row(ddata)
    else:
        table.add_row([data])
    return table