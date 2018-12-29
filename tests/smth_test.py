from smth import Smth

class TestSmthAddToValue():

    def test_returns_new_value(self):
        subject = Smth()
        assert subject.add_to_value(10) == 20

    def test_changes_value(self):
        subject = Smth()
        subject.add_to_value(10)
        assert subject.value == 20
