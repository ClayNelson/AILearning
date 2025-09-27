# Simple Calculator Project

## 🎯 Project Overview
Build a command-line calculator application that performs basic and advanced mathematical operations. This project helps you practice Python fundamentals including functions, loops, exception handling, and user interface design.

## 📋 Requirements
- Basic arithmetic operations (+, -, *, /)
- Advanced operations (square root, exponentiation, percentage)
- Input validation and error handling
- Continuous operation until user chooses to exit
- Clear, user-friendly interface

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Basic understanding of variables, functions, and loops

### Setup
1. Create a new directory: `mkdir calculator-project`
2. Navigate to directory: `cd calculator-project`
3. Create main file: `touch calculator.py`

## 📝 Implementation Steps

### Step 1: Basic Structure
```python
def main():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /, sqrt, **, %")
    
    while True:
        # Calculator logic here
        pass

if __name__ == "__main__":
    main()
```

### Step 2: Basic Operations
Create functions for each operation:
```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return x ** 0.5

def percentage(x, y):
    return (x / y) * 100
```

### Step 3: User Interface
```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def get_operation():
    operations = ['+', '-', '*', '/', 'sqrt', '**', '%', 'exit']
    while True:
        op = input("\nEnter operation (or 'help' for operations list): ").lower()
        if op == 'help':
            print("Available operations:", ', '.join(operations[:-1]))
            continue
        if op in operations:
            return op
        print("Invalid operation! Type 'help' for available operations.")
```

## 🏆 Success Criteria

Your calculator should:
- ✅ Perform all basic arithmetic operations correctly
- ✅ Handle edge cases gracefully (division by zero, etc.)
- ✅ Validate user input and provide helpful error messages
- ✅ Allow continuous calculations until user exits
- ✅ Have clean, readable code with appropriate comments

---

**Ready to calculate?** Start with the basic structure and build your way up!