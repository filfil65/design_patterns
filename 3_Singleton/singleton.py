# I don't like it how they have used 'self' to access the class variable.
# Better to use the class name instead.

class Borg:
    """Borg pattern making the class attributes global"""
    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = Borg._shared_data  # Make it an attribute dictionary
        # self.__dict__ = self._shared_data  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""

    # This essentially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)  # or super().__init__()

        # self._shared_data.update(kwargs)  # Update the attribute dictionary by inserting a new key-value pair
        Borg._shared_data.update(kwargs)  # Update the attribute dictionary by inserting a new key-value pair
        # Or alternatively:
        self.__dict__.update(kwargs)

        # This is why I prefer using Borg rather than self. Because self can refer to both, class and instance attribute
        self._shared_data = [1, 2, 3]

    def __str__(self):
        # return str(self._shared_data)  # Returns the attribute dictionary for printing
        print(str(self._shared_data))  # This will print the instance attribute - this shouldn't be here in
        return str(Borg._shared_data)  # Returns the attribute dictionary for printing


# Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
# Print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
y = Singleton(SNMP="Simple Network Management Protocol")
# Print the object
print(y)
