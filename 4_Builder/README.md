# Builder
It is a solution to an anti-pattern called 'telescoping constructor'.

## Problem
Telescopic constructor occurs when the developer attempts to build an object using an excessive number of constructors.

## Scenario
We are trying to build a car, but we first need to construct all the individual car parts and then assemble them.

# Solution
* A builder pattern brings order to this chaotic process to remove unnecessary complexity in building a complex object.
* The builder partitions the process of building a complex object into the 4 different roles:
1. Director - in charge of actually building the object using the builder object.
2. Abstract Builder class contains all the necessary interfaces required in building an object.
3. Concrete builder inherits from the Abstract Builder, and implements the interfaces for a specific type of product.
4. Product - object being built

## Notes
Builder pattern does not rely on Polymorphism, unlike Factory or Abstract Factory. The focus on the Builder patter 
is rather on decreasing the complexity of building an object through the divide-and-conquer strategy.

Building different types of object becomes easier and cleaner, we simply add another concrete builder.