# Chain of Responsibility
Chain of responsibility opens up various possibilities of processing for a given request.

 Chain of responsibility decouples the request and its processing.

## Problem 
Many different types of processing needs to be done, depending on what the request is.

## Scenario
We receive an integer value, and then use different handlers to find out its range.

## Solution
* Abstract Handler
  * that stores a Successor who will hande the request if it is not handled at the current handler. 
* Concrete Handler(s)
  * Check if they can handle the request. If they can then they return a True value indicating that a request has 
    been handled.

## Related patterns
Composite
