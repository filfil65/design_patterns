import copy


class Prototype:
    
    def __init__(self):
        self._objects = {}  # These are the objects that will be cloned
        
    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj
        
    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]
        
    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))  # Has to be copied, we can't use the same instance
        obj.__dict__.update(attr)  # __dict__ represents all the object attributes
        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object('skylark', c)

c1 = prototype.clone('skylark', color="Black")

print(c1)
