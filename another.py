import os

class Another():
    def __init__(self):
        self.value = 10
    def method(self):
        print(__file__)
        print(os.getcwd())

