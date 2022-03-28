from replit import clear
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  # Calculator
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
    
  operation_symbol = input("Pick an operation: ")
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  
  
  calculation_running = True
  while calculation_running:
    continue_calculation = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculaiton.:\n")
    if continue_calculation == 'y':  
      operation_symbol = input("Pick an operation: ")
      num2 = int(input("What's the next number?: "))
      calculation_function = operations[operation_symbol]
      answer = calculation_function(answer, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
    elif continue_calculation == 'n':
      calculation_running = False
      clear()
      calculator()

calculator()
