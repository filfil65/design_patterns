# Proxy
Proxy becomes very handy when creating an object that is resource intensive.

## Problem
* Postpone object creation as long as possible until absolutely necessary due to the resource intensive nature of 
  the object that we are creating.
* Therefore, there is a need for a light-weight placeholder object which will create this resource intensive object when 
  its creation is necessary.

## Scenario
* We create an instance of this Producer class only when he is available, because only a fixed number of Producer 
  instances is allowed at a time.
* Our proxy in this case is an Artist who is checking if the Producer becomes available for a Guest.

## Solution
* Clients - they interact with the Proxy until the resource intensive object becomes available.
* Therefore, the proxy is responsible for determining whether the resource intensive object is available, or 
  available to be created and then create it.

## Related patterns
Adapter and decorator.

