# PalmaC_ModularCalculator
Modular Calculator for CS 2

# PALMA Python Modular Calculator

A clean, lightweight command-line calculator built in **Python** using a **modular programming architecture**. The program separates the main user-interface loop from the core arithmetic logic using dedicated python functions.

## Features

* **Interactive CLI:** Simple user prompts for inputs and operations.
* **Functional Modularity:** Utilizes separate, specialized Python functions for each math operation.
* **Input Validation:** Gracefully handles invalid operational menu selections and division-by-zero errors.

## 🛠️ How It Works

1. The program prompts you to enter **two numbers**.
2. It displays a menu to choose an operation by entering a number from **1 to 4**:
   * `1`  Calls the **Addition** function (`add`)
   * `2`  Calls the **Subtraction** function (`subtract`)
   * `3`  Calls the **Multiplication** function (`multiply`)
   * `4`  Calls the **Division** function (`divide`)
3. If any other number is entered, the program catches the exception and prints `Invalid operation choice`.

## Function Layout

The core calculation logic is broken down into the following distinct functions:

```python
def add(a, b):       # Returns the sum of two numbers
def subtract(a, b):  # Returns the difference of two numbers
def multiply(a, b):  # Returns the product of two numbers
def divide(a, b):    # Returns the quotient (includes division-by-zero checks)

## Prerequisites


## Installation & Usage


### 2. Run the Program
Launch the entry script using python:
```bash
python main.py
```

##  Execution Example

```text
Enter first number: 20
Enter second number: 5

Choose an operation (1-4):
1. Addition
2. Subtraction
3. Multiplication
4. Division
Choice: 4

Result: 4.0
```

<img width="1229" height="877" alt="Screenshot 2026-10-21 162933" src="https://github.com/user-attachments/assets/0fa7563c-fd39-4bc0-bd64-8dbfb4b61b6f" />
