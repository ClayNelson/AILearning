#!/usr/bin/env python3
"""
Simple Calculator - Complete Solution
A fully functional command-line calculator with error handling.
"""

import math

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, x, y):
        """Add two numbers"""
        return x + y
    
    def subtract(self, x, y):
        """Subtract two numbers"""
        return x - y
    
    def multiply(self, x, y):
        """Multiply two numbers"""
        return x * y
    
    def divide(self, x, y):
        """Divide two numbers"""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y
    
    def power(self, x, y):
        """Calculate x to the power of y"""
        return x ** y
    
    def square_root(self, x):
        """Calculate square root"""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(x)
    
    def percentage(self, x, y):
        """Calculate x percent of y"""
        return (x / 100) * y
    
    def sin(self, x):
        """Calculate sine (x in degrees)"""
        return math.sin(math.radians(x))
    
    def cos(self, x):
        """Calculate cosine (x in degrees)"""
        return math.cos(math.radians(x))
    
    def log(self, x):
        """Calculate natural logarithm"""
        if x <= 0:
            raise ValueError("Cannot calculate logarithm of non-positive number!")
        return math.log(x)
    
    def get_number(self, prompt):
        """Get a valid number from user input"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def get_operation(self):
        """Get a valid operation from user input"""
        operations = ['+', '-', '*', '/', 'sqrt', '**', '%', 'sin', 'cos', 'log', 
                     'help', 'history', 'clear', 'exit']
        
        while True:
            op = input("\n🔢 Enter operation: ").lower().strip()
            
            if op == 'help':
                self.show_help()
                continue
            elif op == 'history':
                self.display_history()
                continue
            elif op == 'clear':
                self.clear_history()
                continue
            elif op in operations:
                return op
            else:
                print("❌ Invalid operation! Type 'help' for available operations.")
    
    def show_help(self):
        """Display help information"""
        print("\n" + "=" * 50)
        print("📚 CALCULATOR HELP")
        print("=" * 50)
        print("Basic Operations:")
        print("  +     : Addition")
        print("  -     : Subtraction")
        print("  *     : Multiplication")
        print("  /     : Division")
        print("\nAdvanced Operations:")
        print("  **    : Exponentiation")
        print("  sqrt  : Square root")
        print("  %     : Percentage")
        print("  sin   : Sine (degrees)")
        print("  cos   : Cosine (degrees)")
        print("  log   : Natural logarithm")
        print("\nSpecial Commands:")
        print("  help    : Show this help")
        print("  history : Show calculation history")
        print("  clear   : Clear history")
        print("  exit    : Exit calculator")
        print("=" * 50)
    
    def display_history(self):
        """Display calculation history"""
        if not self.history:
            print("📝 No calculations in history yet!")
        else:
            print("\n" + "=" * 40)
            print("📝 CALCULATION HISTORY")
            print("=" * 40)
            for i, calc in enumerate(self.history[-10:], 1):  # Show last 10
                print(f"{i:2d}. {calc}")
            print("=" * 40)
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        print("✅ History cleared!")
    
    def add_to_history(self, calculation):
        """Add calculation to history"""
        self.history.append(calculation)
    
    def perform_calculation(self, operation, num1, num2=None):
        """Perform the actual calculation"""
        try:
            if operation == '+':
                result = self.add(num1, num2)
                calc_str = f"{num1} + {num2} = {result}"
            elif operation == '-':
                result = self.subtract(num1, num2)
                calc_str = f"{num1} - {num2} = {result}"
            elif operation == '*':
                result = self.multiply(num1, num2)
                calc_str = f"{num1} × {num2} = {result}"
            elif operation == '/':
                result = self.divide(num1, num2)
                calc_str = f"{num1} ÷ {num2} = {result}"
            elif operation == '**':
                result = self.power(num1, num2)
                calc_str = f"{num1}^{num2} = {result}"
            elif operation == '%':
                result = self.percentage(num1, num2)
                calc_str = f"{num1}% of {num2} = {result}"
            elif operation == 'sqrt':
                result = self.square_root(num1)
                calc_str = f"√{num1} = {result}"
            elif operation == 'sin':
                result = self.sin(num1)
                calc_str = f"sin({num1}°) = {result}"
            elif operation == 'cos':
                result = self.cos(num1)
                calc_str = f"cos({num1}°) = {result}"
            elif operation == 'log':
                result = self.log(num1)
                calc_str = f"ln({num1}) = {result}"
            
            print(f"\n✅ {calc_str}")
            self.add_to_history(calc_str)
            
        except ValueError as e:
            print(f"\n❌ Error: {e}")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
    
    def run(self):
        """Main calculator loop"""
        print("=" * 50)
        print("    🧮 SIMPLE CALCULATOR")
        print("=" * 50)
        print("Type 'help' for available operations")
        print("Type 'exit' to quit")
        print("=" * 50)
        
        while True:
            operation = self.get_operation()
            
            if operation == 'exit':
                print("\n👋 Thank you for using the calculator!")
                print(f"📊 Total calculations performed: {len(self.history)}")
                break
            
            # Operations that need only one number
            if operation in ['sqrt', 'sin', 'cos', 'log']:
                num1 = self.get_number("Enter number: ")
                self.perform_calculation(operation, num1)
            
            # Operations that need two numbers
            elif operation in ['+', '-', '*', '/', '**', '%']:
                num1 = self.get_number("Enter first number: ")
                num2 = self.get_number("Enter second number: ")
                self.perform_calculation(operation, num1, num2)

def main():
    """Main function"""
    calculator = Calculator()
    calculator.run()

if __name__ == "__main__":
    main()