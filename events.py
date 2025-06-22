from pynput.keyboard import Listener
from pynput import keyboard


class MyListener:
    def __init__(self):
        self.running = False
        self.key_holder = ""
        self.listener = None
        self.ctrl_pressed = False
        self.shift_pressed = False

    """
    this function needs to start the listener thread
    """

    def start_run_and_listener(self):
        self.running = True
        self.listener = keyboard.Listener(on_press=self.catch_key_press)
        self.listener.start()

    """
        this function needs to wait until the program stops
    """

    def start_join(self):
        self.listener.join()

    """
    handel the pressing on the keyboard
    """

    def catch_key_press(self, key):
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = True
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            self.shift_pressed = True
        try:
            close = (self.ctrl_pressed, self.shift_pressed, key.char)
            match close:
                case (True, True, 'c'):
                    self.temp_fun()
                case _:
                    self.key_holder += key.char
        except AttributeError:
            match key:
                case keyboard.Key.esc:
                    self.stop_program()
                case keyboard.Key.space:
                    self.key_holder += " "
                case keyboard.Key.enter:
                    self.key_holder += " \n "
                case keyboard.Key.up:
                    self.key_holder += " "
                case keyboard.Key.right:
                    self.key_holder += " "
                case keyboard.Key.left:
                    self.key_holder += " "
                case keyboard.Key.up:
                    self.key_holder += " \n "
                case keyboard.Key.backspace:
                    self.key_holder = self.key_holder[:-1]

    def hold_press(self):
        return self.key_holder

    def stop_program(self):
        self.running = False
        self.listener.stop()

    # def temp_fun(self):
    #     return True
