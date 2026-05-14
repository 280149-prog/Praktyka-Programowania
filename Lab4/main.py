from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TV:
    def on(self):
        print("ON")
    def off(self):
        print("OFF")


class TurnOn(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.on()

class TurnOff(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.off()

tv = TV()
cmd1 = TurnOn(tv)
cmd1.execute()
cmd2 = TurnOff(tv)
cmd2.execute()