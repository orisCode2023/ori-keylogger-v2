import datetime
import threading

timer_running = True
def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def timer():
    if timer_running:
        time = threading.Timer(10.0, timer)
        time.start()



def stop_timer():
    global timer_running
    timer_running = False


