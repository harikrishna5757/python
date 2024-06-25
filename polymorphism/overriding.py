class Language:
    def __init__(self):
        self.oops = True
        self.syntax = "same"

    def detail(self):
        pass


class Python(Language):
    def __init__(self):
        super().__init__()
        self.language = "python"
        self.syntax = "different"

    def detail(self):
        print(self.oops, self.syntax, self.language)


class Java(Language):
    def __init__(self):
        super().__init__()
        self.language = "java"
        self.syntax = "different"

    def detail(self):
        print(self.oops, self.syntax, self.language)


java = Java()
java.detail()
python = Python()
python.detail()
