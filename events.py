from pynput.keyboard import Listener
from pynput import keyboard


class MyListener:
    def __init__(self):
        self.running = False
        self.key_holder = ""
        self.listener = None

    def start_run_and_listener(self):
        self.running = True
        self.listener = keyboard.Listener(on_press=self.catch_key_press)
        self.listener.start()
        self.listener.join()

    def catch_key_press(self, key):
        match key:
            case keyboard.Key.esc:
                self.stop_program()
            case keyboard.Key.space:
                self.key_holder += " "
            case keyboard.Key.enter:
                self.key_holder += "\n"
        try:
            self.key_holder += key.char
        except AttributeError:
            pass

    def hold_press(self):
        return self.key_holder

    def stop_program(self):
        self.running = False
        self.listener.stop()


lst = MyListener()
lst.start_run_and_listener()
s = lst.hold_press()
print(s)
