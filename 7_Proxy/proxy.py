import time


class Producer:
	"""Define the 'resource-intensive' object to instantiate!"""

	def produce(self):
		print("Producer is working hard!")

	def meet(self):
		print("Producer has time to meet you now!")


class Proxy:
	"""Define the 'relatively less resource-intensive' proxy to instantiate as a middleman."""

	def __init__(self):  
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		"""Check if Producer is available"""
		print("Artist checking if Producer is available ...")

		if self.occupied == 'No':
			# If the producer is available, create a producer object!
			self.producer = Producer()
			time.sleep(2)

			# Make the producer meet the guest!
			self.producer.meet()
			
		else:
			# Otherwise, don't instantiate a producer
			time.sleep(2)
			print("Producer is busy!")


# Instantiate a Proxy
p = Proxy()

# Make the proxy: Artist produce until Producer is available
p.produce()

# Change the state to 'occupied'
p.occupied = 'Yes'  # Might be better to put that into the produce() method?

# Make the Producer produce
p.produce()

# But what if you need to perform numerous operations with the Producer? Should Proxy then have identical interface as
# the Producer? If yes, then each method could be decorated with "if available - else".

# What is halfway through using the Producer it becomes unavailable and then available again? The proxy would
# re-instantiate the Producer and potentially lose state.

# It would be cool if the Proxy could become the Producer once the Producer is instantiated.
# Or why not make the Producer a 'proxy' of itself and only initialize resource intensive parts when ready?
# - This can be done by adding the __getattr__ which returns from the Producer object (see adapter.py).
