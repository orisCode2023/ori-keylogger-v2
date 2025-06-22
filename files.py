class MyFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.create_or_check_file()

    def create_or_check_file(self):
        try:
            with open(self.file_name, "x"):
                pass
        except FileExistsError:
            pass
        return self

    def write_to_file(self, input_key):
        with open(self.file_name, "a") as file:
            file.write(input_key + " ")
        return self

    def read_file(self):
        with open(self.file_name, "r") as file:
            return file.read()



