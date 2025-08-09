# MIA Summer Training - AI SUB-TEAM Tasks

**Program created and programmed by:** Yassin Khaled, CCE28

This repository contains three Python programming tasks completed as part of the MIA Summer training program for the AI SUB-TEAM.

## Table of Contents
- [Task 1.1: Gear Display System](#task-11-gear-display-system)
- [Task 1.2: String Encoding/Decoding System](#task-12-string-encodingdecoding-system)  
- [Task 1.3: F1 Race Simulation](#task-13-f1-race-simulation)

---

## Task 1.1: Gear Display System

### Description
A program that displays gear numbers (0-8) using ASCII art patterns on a 5x4 grid.

### Features
- **Visual Gear Display**: Each gear number is represented by a unique ASCII pattern
- **Neutral Gear**: Gear 0 is labeled as "Neutral Gear"
- **Input Validation**: Handles invalid inputs and non-numeric entries
- **Exit Functionality**: Enter -1 to exit the program

### How to Run
```bash
python Task1.1.py
```

### Usage Example
```
Enter the gear number (0-8, or -1 to exit): 3
Gear 3
####
   #
####
   #
####
Gear display complete.
```

### Requirements Completed
- ✅ Display gear based on gear number
- ✅ Initialize 5x4 grid for gear display
- ✅ Loop for continuous user input
- ✅ Neutral gear represented by 0
- ✅ Exit when user enters -1

---

## Task 1.2: String Encoding/Decoding System

### Description
A class-based system that encodes and decodes strings using a word reversal algorithm.

### Features
- **Universal Encoding**: Works with any string including empty strings, numbers, and special characters
- **Reversible Process**: Perfect encoding/decoding cycle maintains original data
- **Flexible Input**: Accepts multiple strings as arguments
- **Demonstration**: Built-in testing with F1 commands

### How to Run
```bash
python Task1.2.py
```

### Usage Example
```
Enter a list of commands (Quotes for each word ,with commas in between): "Box", "Box", "Stay out"
Input: ["Box", "Box", "Stay out"]
Output: ['Box', 'Box', 'Stay out']
```

### Algorithm
- **Encoding**: Reverses each word and concatenates into single string
- **Decoding**: Uses word lengths to split and reverse back to original

### Requirements Completed
- ✅ Implement encode and decode functions
- ✅ Handle any possible string input
- ✅ Demonstrate with F1 commands
- ✅ Show encoding and decoding process

---

## Task 1.3: F1 Race Simulation

### Description
An object-oriented racing simulation featuring two F1 drivers with unique moves and abilities.

### Features
- **OOP Design**: Full implementation of inheritance, encapsulation, abstraction, and polymorphism
- **Turn-Based Combat**: Drivers alternate between attacking and defending
- **Resource Management**: Fuel consumption and tire health tracking
- **Unique Drivers**: Max Verstappen and Hassan Mostafa with different move sets
- **Limited Abilities**: Special moves have usage restrictions

### How to Run
```bash
python Task1.3.py
```

### Drivers & Moves

#### Max Verstappen
**Offensive Moves:**
- DRS Boost: 45 fuel, 12 damage
- Red Bull Surge: 80 fuel, 20 damage  
- Precision Turn: 30 fuel, 8 damage

**Defensive Moves:**
- Brake Late: 25 fuel, 30 damage reduction
- ERS Deployment: 40 fuel, 50 damage reduction (3 uses max)

#### Hassan Mostafa
**Offensive Moves:**
- Turbo Start: 50 fuel, 10 damage
- Mercedes Charge: 90 fuel, 22 damage
- Corner Mastery: 25 fuel, 7 damage

**Defensive Moves:**
- Slipstream Cut: 20 fuel, 40 damage reduction
- Aggressive Block: 35 fuel, 100 damage reduction (2 uses max)

### Game Mechanics
- **Starting Stats**: 100 tire health, 500 fuel
- **Win Conditions**: Opponent reaches 0 tire health or 0 fuel
- **Damage Calculation**: `final_damage = max(0, attack_damage - defense_reduction)`
- **Role Switching**: Attacker and defender roles alternate each round

### OOP Concepts Implemented
- **Abstract Base Class**: `Driver` class with abstract methods
- **Inheritance**: `Verstappen` and `Mostafa` inherit from `Driver`
- **Encapsulation**: Private attributes with property getters/setters
- **Polymorphism**: Different implementations of abstract methods
- **Composition**: `Race` class contains `Driver` objects

### Requirements Completed
- ✅ Create driver classes with unique properties
- ✅ Implement offensive and defensive moves
- ✅ Create intelligent move selector
- ✅ Implement move execution logic with state updates

---

## Technical Implementation

### Programming Concepts Used
- **Object-Oriented Programming**: Classes, inheritance, encapsulation, abstraction
- **Error Handling**: Try-catch blocks and input validation
- **Data Structures**: Lists, dictionaries, tuples
- **Control Flow**: Loops, conditionals, function calls
- **String Manipulation**: Slicing, joining, formatting

### File Structure
```
├── Task1.1.py          # Gear display system
├── Task1.2.py          # String encoding/decoding
├── Task1.3.py          # F1 race simulation
└── README.md           # This documentation
```

### Dependencies
- Python 3.x
- Built-in modules only:
  - `abc` (Abstract Base Classes)
  - `random` (Random number generation)

---

All programs include user input handling and demonstrate their functionality with interactive examples.

---

**Author**: Yassin Khaled, CCE28  
**Program**: MIA Summer Training - AI SUB-TEAM  
**Completion Date**: 2025
