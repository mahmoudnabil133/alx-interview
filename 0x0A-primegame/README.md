# 0x0A. Prime Game

## Project Overview

This project is part of the ALX Specializations curriculum, focusing on algorithmic challenges using Python. The task is to determine the winner of a game played between two players, Maria and Ben, based on the strategic removal of prime numbers from a set of consecutive integers.

### Average Score: 96.03%
- **Weight**: 1
- **Start Date**: Sep 2, 2024 6:00 AM
- **End Date**: Sep 6, 2024 6:00 AM
- **Checker Released**: Sep 3, 2024 6:00 AM

## Project Details

### Concepts Needed:
- **Prime Numbers**:
  - Understand prime numbers and how to identify them efficiently within a range.
  
- **Sieve of Eratosthenes**:
  - An efficient algorithm for finding all prime numbers up to a given limit.
  
- **Game Theory**:
  - Basic principles of competitive games and the concept of optimal play.
  - Strategies that lead to a win or loss based on the game’s rules.
  
- **Dynamic Programming/Memoization**:
  - Using previous results to optimize future calculations.

- **Python Programming**:
  - Loops and conditional statements.
  - Arrays and lists for managing the game state.

### Resources:
- **Prime Numbers and Sieve of Eratosthenes**:
  - [Khan Academy: Prime Numbers](https://www.khanacademy.org)
  - [Sieve of Eratosthenes in Python](https://example.com)
  
- **Game Theory Basics**:
  - [Game Theory Introduction](https://example.com)
  
- **Dynamic Programming**:
  - [What Is Dynamic Programming With Python Examples](https://example.com)
  
- **Python Official Documentation**:
  - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Requirements:
- **General**:
  - Allowed editors: `vi`, `vim`, `emacs`.
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3).
  - All files should end with a new line.
  - The first line of all files should be `#!/usr/bin/python3`.
  - A `README.md` file at the root of the project folder is mandatory.
  - Code should follow PEP 8 style (version 1.7.x).
  - All files must be executable.

## Tasks

### 0. Prime Game (Mandatory)

Maria and Ben are playing a game with a set of consecutive integers starting from 1 up to and including `n`. They take turns choosing a prime number from the set and removing that number and its multiples. The player who cannot make a move loses the game.

They play `x` rounds, where `n` may be different for each round. Maria always goes first, and both players play optimally. The task is to determine the winner of each game and return the name of the player who won the most rounds.

#### Prototype:
```python
def isWinner(x, nums)
