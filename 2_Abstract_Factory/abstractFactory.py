class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"


class DogFactory:
	"""Concrete Factory."""

	def get_pet(self):
		"""Returns a Dog object."""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food object."""
		return "Dog Food!"


class PetStore:
	"""PetStore houses our Abstract Factory."""

	def __init__(self, pet_factory=None):
		"""pet_factory is our Abstract Factory."""
		self._pet_factory = pet_factory

	def show_pet(self):
		"""Utility method to display the details of the objects returned by the AbstractFactory (e.g. DogFactory)."""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()
		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))


# Create a Concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
# This abstracts the concrete factory, thus allowing us to use it without differentiating between Pet types.
shop = PetStore(factory)

# Invoke the utility method to show the details of our pet
shop.show_pet()

# Adding a Cat and Cat Factory would be trivial to do.

# Having the concrete Dog and Cat factories allows you to parameterize your pets, e.g. by breed.
# The Abstract factory (Pet Store) then allows you to use your Cats and Dogs in a generic/abstract way.
