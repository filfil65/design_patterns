class Subject:  # Represents what is being 'observed'

	def __init__(self):
		# This is where references to all the observers are being kept
		# Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers
		self._observers = []

	def attach(self, observer):
		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	def notify(self, modifier=None):
		for observer in self._observers:
			if modifier != observer:  # Don't notify the observer who is updating the temp - somehow it can do that
				observer.update(self)  # Alert the observers


class ReactorCore(Subject):

	def __init__(self, name=""):
		Subject.__init__(self)
		self._name = name
		self._temp = 0

	@property
	def temp(self):
		return self._temp

	@temp.setter
	def temp(self, temp):
		self._temp = temp
		self.notify()  # Notify the observers whenever somebody changes the core temperature


# We should really have an abstract Observer class as well.
class TempViewer:
	def update(self, subject):
		# Alert method that is invoked when the notify() method in a concrete subject is invoked
		print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


# Let's create our subjects
c1 = ReactorCore("Core 1")
c2 = ReactorCore("Core 2")

# Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# Let's change the temperature of our first core
c1.temp = 80
c1.temp = 90

c2.temp = 100
