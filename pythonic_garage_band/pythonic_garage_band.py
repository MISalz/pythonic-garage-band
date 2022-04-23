class Band:
    pass


class Musician():
    pass


class Guitarist():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist():
    pass


class Drummer():
    # were creating a new instantiation of drummer class with property name
    def __init__(self, name):
        # assigning a property =
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
