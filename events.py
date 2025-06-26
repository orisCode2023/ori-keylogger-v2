from pynput.keyboard import Listener
from pynput import keyboard


class MyListener:
    def __init__(self):
        self.running = False
        self.key_holder = ""
        self.listener = None
        self.ctrl_pressed = False
        self.shift_pressed = False
        self.close_button = False

    """
    this function needs to start the listener thread
    """

    def start_run_and_listener(self):
        self.running = True
        self.listener = keyboard.Listener(on_press=self.catch_key_press,
                                          on_release=self.catch_close_button_release)
        self.listener.start()

    """
    this function needs to wait until the program stops
    """

    def start_join(self):
        self.listener.join()

    """
    handel the shortcut to shutdown the project
    """

    def catch_close_button(self, key):
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = True
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            self.shift_pressed = True
        elif self.shift_pressed and self.ctrl_pressed and key.char == 'c':
            self.close_button = True


    def catch_close_button_release(self, key):
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = False
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            self.shift_pressed = False

    """
    handel the pressing on the keyboard
    """

    def catch_key_press(self, key):
        self.catch_close_button(key)

        try:
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
                case keyboard.Key.down:
                    self.key_holder += " \n "
                case keyboard.Key.backspace:
                    if self.key_holder:
                        self.key_holder = self.key_holder[:-1]

    """
    hold all the pressing 
    """

    def hold_press(self):
        return self.key_holder

    """
    stop the listener
    """

    def stop_program(self):
        self.running = False
        self.listener.stop()
