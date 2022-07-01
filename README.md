# Design Patterns
For further learning, see https://github.com/faif/python-patterns

## Why?
When developing software you might encounter the same problem over and over. Design patterns are well knows and 
accepted solutions to those problems. 
* There is no need to reinvent the wheel.
* Reuse of design ideas and best practices yield lower cost and higher quality.

## Characteristics 
* Language neutral
* Dynamic - new patterns come out and old get revised
* Intentionally incomplete by design to encourage customization

## Types
* Creational
  * Used to create objects in a systematic way
  * Flexibility
  * Different subtypes can be created during runtime
* Structural
  * Establishes useful relationships between software components in certain configurations
  * The goal is to accomplish functional and non-functional requirements
  * Different goals yield to different structures 
* Behavioural
  * Best practices of object interaction
  * The goal is to define the protocol for communication

Design patterns make use of OOP mechanisms:
* Creational => Polymorphism
* Structural => Inheritance
* Behavioural => Methods and their signatures

The different types can then be linked together using interfaces. 

# Pattern Context
To use patterns effectively, you need to know the context in which they work bes.t Also important to know what is 
used oto describe a pattern context. 

Pattern context consists of the following:
* Participants
  * **Classes** involved to form a design pattern
  * The above classes play different **roles** to accomplish the goal of the pattern
* Quality attributes
  * Non-functional requirements such as usability, modifiability, reliability, etc.
  * They have an affect of the entire software and can only be addressed by architectural solutions.
* Forces
  * Various factors or trade-offs to consider
  * Manifested in quality attributes
  * If forces are not well reasoned, you might end up with unintended consequences
* Consequences
  * Side effects, e.g. better security but worse performance.
  * The decision maker will have to choose which pattern to use.
  * Sometimes patterns can give more problems than they solve.

# Pattern Language
Patterns are described using the following language:

* **Name** - capture the gist of the pattern, meaningful and memorable.
* **Context** - provides a scenario, and when to use and not to use the pattern.
* **Problem** - the design challenge the pattern is trying to solve
* **Solution** - specifies the structure(relationships between elements) and behaviour(interaction) of the pattern
* **Related Patterns** - list of other patterns used with the given patterns, and similar but different patterns and 
  their differences.