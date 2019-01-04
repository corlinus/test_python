from another import Another

class Smth():
    def __init__(self):
        self.value = 10
        self.another = Another()

    def add_to_value(self, b):
        print(__file__)
        self.value += 10
        return self.value
