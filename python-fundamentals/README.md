# Python Fundamentals Learning Path

## 🎯 Overview
This path is designed for complete beginners or those wanting to strengthen their Python foundations. No prior programming experience required!

## 📋 Prerequisites
- Basic computer literacy
- Willingness to learn and practice consistently
- 5-10 hours per week commitment

## 🚀 Setup Instructions

### 1. Install Python
- Download Python 3.9+ from [python.org](https://python.org)
- Verify installation: `python --version`

### 2. Choose Your Development Environment
**Option A: VS Code (Recommended for beginners)**
- Install VS Code
- Install Python extension
- Install Code Runner extension

**Option B: PyCharm Community Edition**
- Free IDE with excellent Python support

**Option C: Jupyter Notebooks**
- Great for data science and experimentation
- Install: `pip install jupyter notebook`

### 3. Create Your First Project
```bash
mkdir my-python-learning
cd my-python-learning
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate
```

## 📚 Week 1-2: Programming Basics

### Day 1-2: Getting Started
- [ ] **Video**: Watch "Python in 5 Minutes" overview
- [ ] **Practice**: Print "Hello, World!" in 5 different ways
- [ ] **Read**: Variables and naming conventions
- [ ] **Exercise**: Create variables for your personal information

### Day 3-4: Data Types and Operations
```python
# Practice these concepts
name = "Your Name"           # String
age = 25                     # Integer
height = 5.8                 # Float
is_student = True            # Boolean
hobbies = ["reading", "coding"]  # List
```
- [ ] **Exercises**: 
  - Create a personal profile using all data types
  - Practice string formatting and manipulation
  - Work with numbers and mathematical operations

### Day 5-7: Control Structures
```python
# If statements
if age >= 18:
    print("You can vote!")
else:
    print("Not old enough to vote yet")

# Loops
for hobby in hobbies:
    print(f"I enjoy {hobby}")

for i in range(1, 11):
    print(f"Number: {i}")
```
- [ ] **Project Start**: Simple Calculator
  - Basic arithmetic operations
  - User input handling
  - Input validation

### Day 8-14: Functions and Code Organization
```python
def greet_user(name, age):
    """Greet a user with their name and age."""
    return f"Hello {name}, you are {age} years old!"

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width
```
- [ ] **Exercises**:
  - Create utility functions for your calculator
  - Build a function library for common operations
- [ ] **Project Complete**: Enhanced Calculator with Functions

**Week 1-2 Project: Simple Calculator**
```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation: ")
            num2 = float(input("Enter second number: "))
            
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation!")
                continue
                
            print(f"Result: {result}")
            
            if input("Continue? (y/n): ").lower() != 'y':
                break
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()
```

## 📚 Week 3-4: Intermediate Python

### Data Structures Deep Dive
```python
# Lists - ordered, mutable
students = ["Alice", "Bob", "Charlie"]
students.append("Diana")
students.remove("Bob")

# Dictionaries - key-value pairs
student_grades = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92
}

# Sets - unique elements
unique_subjects = {"Math", "Science", "English"}

# Tuples - ordered, immutable
coordinates = (10.5, 20.3)
```

### File Operations and Error Handling
```python
# Reading files
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")

# Writing files
tasks = ["Learn Python", "Build a project", "Get a job"]
with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(f"- {task}\n")
```

### Object-Oriented Programming Introduction
```python
class Task:
    def __init__(self, title, description, priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
        print(f"Task '{self.title}' marked as complete!")
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} {self.title} ({self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task.title}")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return
        
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    
    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
        else:
            print("Invalid task number!")
```

**Week 3-4 Project: Personal Task Management System**

Complete implementation with file persistence, task priorities, and a simple CLI interface.

## 📚 Week 5-6: Python for Data Science

### NumPy Fundamentals
```python
import numpy as np

# Arrays and operations
numbers = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4], [5, 6]])

# Mathematical operations
mean_value = np.mean(numbers)
matrix_sum = np.sum(matrix, axis=0)
```

### Pandas for Data Manipulation
```python
import pandas as pd

# Creating DataFrames
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}
df = pd.DataFrame(data)

# Data operations
df['Age Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
filtered_df = df[df['Age'] > 25]
```

### Data Visualization with Matplotlib
```python
import matplotlib.pyplot as plt

# Simple plots
ages = [25, 30, 35, 40, 45]
salaries = [40000, 50000, 60000, 70000, 80000]

plt.figure(figsize=(8, 6))
plt.plot(ages, salaries, marker='o')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()
```

**Week 5-6 Project: Data Analysis of Real-World Dataset**

Analyze a dataset of your choice (weather data, stock prices, sports statistics) and create visualizations to tell a story with the data.

## 🎯 Learning Tips

1. **Practice Daily**: Even 30 minutes daily is better than 5 hours once a week
2. **Code Along**: Don't just read - type out every example
3. **Modify Examples**: Change values, add features, break things and fix them
4. **Ask Questions**: Use forums like Stack Overflow, Reddit r/learnpython
5. **Build Projects**: Apply concepts immediately in real projects

## 📝 Assessment Checklist

By the end of this path, you should be able to:
- [ ] Write clean, readable Python code
- [ ] Use all major data structures effectively
- [ ] Handle files and exceptions gracefully
- [ ] Create basic classes and objects
- [ ] Work with data using NumPy and Pandas
- [ ] Create simple data visualizations
- [ ] Debug your own code effectively
- [ ] Follow Python best practices and PEP 8 style guide

## 🎓 Next Steps

After completing this path, you're ready for:
- **AI/ML Beginner Path** - Start building intelligent applications
- **Web Development** - Flask or Django web frameworks
- **Data Science Specialization** - Deep dive into analytics and visualization
- **Automation and Scripting** - Automate repetitive tasks

## 📚 Recommended Resources

### Books
- "Python Crash Course" by Eric Matthes (Beginner-friendly)
- "Effective Python" by Brett Slatkin (Best practices)

### Online Courses
- freeCodeCamp Scientific Computing with Python
- Coursera Python for Everybody Specialization

### Practice Platforms
- HackerRank Python domain
- LeetCode (for algorithm practice)
- Python.org's official tutorial

---

Remember: Programming is a skill that develops with practice. Don't rush through the material - take time to understand each concept thoroughly!