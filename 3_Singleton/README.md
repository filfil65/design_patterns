# Singleton
There are many ways to implement a singleton patterns. Here we will be using the Borg design pattern.

## Problem
* When you would like to allow only one object to be instantiated from a class.
* A global variable is also a singleton.

## Scenario
We need an information cache that is shared and used by multiple objects.
By storing all the required info in one place, you don't need to keep fetching it from it source.

Modules in python are treated as singletons, and can be shared by multiple objects.

## Alternative to Borg
Alternatively, in your Singleton class, modify the `__new__()` method to always return the first instance that was 
created. The first instance can be stored as a class var.