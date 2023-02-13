class Animal:
    def __init__(self):
        self.eyes = 2

    def breathing(self):
        print(" inhale exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathing(self):
        super().breathing()
        print("doing in water")

    def living(self):
        print("mostly in water")


nemo=Fish()
nemo.breathing()
print(nemo.eyes)