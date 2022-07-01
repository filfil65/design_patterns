# Iterator
Iterator pattern allows the client to have sequential access to the elements of an aggregate object without 
exposing its underlying structure.

## Problem
Some developers overcrowd the traversal interfaces of aggregate objects for every possible way of iteration.

## Scenario
We will build our own iterator using Python's zip() iterator to iterate through a list of German counting words.
It will only iterate up to a certain point based on the client input.

## Solution
An iterator isolates access and traversal features from an aggregate object. 
An iterator provides an interface for accessing the elements of an aggregate object. 
An iterator keeps track of the objects being traversed. 
One of the recommended solutions is to make the aggregate object create an iterator for a client

Python does provide a built-in iterator which makes building custom iterators much easier.

## Related patterns
Composite
