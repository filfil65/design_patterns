#  Observer
Observer establishes a one-to-many relationship between a Subject and multiple Observers. 

## Problem
A Subject object needs to be monitored.
Observer objects need to be notified when there is a change in the Subject. 

## Scenario
We need to be able to keep track of core temperatures in a reactor at a power plant.
When there is a change in the core temperature, the registered Observers need to be notified.

## Solution
* Subject - an abstract class which has interfaces that allow:
  * Attach an Observer
  * Detach an Observer
  * Notify an Observer
* Concrete subjects that inherit from the Subject abstract class

## Related patterns
Singleton
