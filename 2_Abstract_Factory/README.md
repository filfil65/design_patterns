# Abstract Factory
* Especially useful when the client expects to receive a family of related objects at a given time, but doesn't
have to know which family it is until runtime.


## Why?
* The user expectation yields multiple, related objects.

## Scenario
We will build a Pet Factory which includes a Dog and Cat factories. Those factories produce dog and cat food.

## Solution will consist of:
* Abstract factory: pet factory
* Concrete factory: dog factory and cat factory
* Abstract product
* Concrete product: dog and dog food; cat and cat food

We are able to create the abstract factory without the use of inheritance thanks to Python being a dynamically typed 
language and therefore does not require abstract classes.

Abstract factory is related to factory method, and concrete factories are often singletons.