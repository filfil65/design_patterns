from functools import wraps


def make_blink(function):
	"""Defines the decorator."""

	# This makes the decorator transparent in terms of its name and docstring
	# i.e. the wrapped function doesn't become the wrapper
	@wraps(function)
	# Define the inner function
	def decorator():
		# Grab the return value of the function being decorated
		ret = function() 

		# Add new functionality to the function being decorated
		return "".join(["<blink>", ret, "</blink>"])

	return decorator


@make_blink  # Apply the decorator here!
def hello_world():
	"""Original function!"""
	return "Hello, World!"


# Check the result of decorating
print(hello_world())

# Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

# Check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)

print("\n\n")


# This demonstrates why you should use @wrap
def decorator_with_no_wrap(func):
	def wrapper():
		return func() + " No! It's Bob!"
	return wrapper


test = decorator_with_no_wrap(hello_world)
print(test())
print(test.__name__)  # = wrapper
print(test.__doc__)  # = None
