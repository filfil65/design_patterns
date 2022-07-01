# Strategy
Strategy pattern offers a family of interchangeable algorithms to a client.

## Problem
There is a need for dynamically changing the behaviour of an object.

## Scenario
We offer an abstract Strategy class with a default set of behaviours. 
When there is a need we provide another variation of the Strategy class, by dynamically replacing its default 
method with a new one.

## Solution
Python allows adding methods dynamically by using the 'types' module.

## Related patterns
