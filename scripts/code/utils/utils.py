from datetime import datetime

def convert_datetime(date, format='%y%m%d'):
    return datetime.strptime(date, format)