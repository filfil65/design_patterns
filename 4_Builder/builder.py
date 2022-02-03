class Director:
    """Director - the one that actually builds the car."""

    def __init__(self, builder):
        self._builder = builder  # This is the concrete builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    """Abstract Builder.

    Creates the car object and keeps it as its attribute.
    """

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts.

    Provides additional methods to be used by the Director class.
    """

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class Car:
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)
