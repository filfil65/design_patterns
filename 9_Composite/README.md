# Composite
Composite pattern maintains a tree data structure to represent part-whole relationships.
https://refactoring.guru/design-patterns/structural-patterns

## Problem
We want to build a recursive tree data structure so that an element of a tree can have its own sub-elements. 

e.g. menu -> submenu -> sub-submenu

## Scenario
Display a restaurant manu and submenu using this Composite pattern.

## Solution
Three classes:

- Component - Is an abstract clas.
- Child - Concrete class that inherits from component class.
- Composite - Also inherits from component. It maintains the Child objects by adding or removing them from the 
  tree-data structure. 

## Related patterns
- Decorator
- Iterator
- Visitor
 