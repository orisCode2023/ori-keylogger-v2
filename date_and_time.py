import datetime

def get_time():
    return datetime.datetime.now()

def compare_time():
    time = datetime.datetime.now()
    return time > get_time()


