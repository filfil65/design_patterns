# Adapter
Adapter converts an interface of a class into another that the client is expecting.

## Problem
* Interfaces are incompatible between a client and a server.

## Scenario
We have two related objects which have two different methods for speaking:
* Korean: speak_korean()
* English: speak_english()

But client expects a uniform method for speaking:
* Client: speak()

## Solution
Use the adapter pattern to translate the method name between the client and the server.

## Related patterns
Bridge, decorator.

