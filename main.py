OPERATIONS = "+-*/="
OPERATION_PRECEDENCE = {"*": 1, "/": 1, "+": 2, "-": 2}
def parse_equation(equation):
  equation = [char for char in equation]
  parsed_equation = []
  left = 0

  while left < len(equation):
    right = left
    if equation[left] in OPERATIONS:
      parsed_equation.append(equation[left])
      left += 1
    else:
      number = ""
      while right < len(equation) and equation[right].isnumeric():
        number += f"{equation[right]}"
        right += 1
      while right < len(equation) and equation[right].isalpha():
        number += f"{equation[right]}"
        right += 1
      parsed_equation.append(number)
      left = right
  return parsed_equation
      

class Algebra:
  def __init__(self, equation):
    self.equation = str(equation)
    self.list_of_terms = parse_equation(equation)

  def __str__(self):
    return self.equation
  
  def add(self, term1, term2):
    return float(term1) + float(term2)
  
  def subtract(self, term1, term2):
    return float(term1) - float(term2)
  
  def multiply(self, term1, term2):
    return float(term1) * float(term2)

  def divide(self, term1, term2):
    return float(term1) / float(term2)
  
  def simple_equation(self, list):
    if list[1] == "+":
      return self.add(list[0], list[2])
    if list[1] == "-":
      return self.subtract(list[0], list[2])
    if list[1] == "*":
      return self.multiply(list[0], list[2])
    if list[1] == "/":
      return self.divide(list[0], list[2])
    
  def simple_stack_equation(self):
    self.operands_stack = []
    self.operations_stack = []
    for i in range(len(self.list_of_terms)):
      if self.list_of_terms[i] in OPERATIONS: 
        if len(self.operations_stack) >= 1 and OPERATION_PRECEDENCE[self.list_of_terms[i]] >= OPERATION_PRECEDENCE[self.operations_stack[-1]]:
          equation = self.simple_equation([self.operands_stack.pop(0), self.operations_stack.pop(0), self.operands_stack.pop(0)])
          self.operands_stack.append(equation)
        self.operations_stack.append(self.list_of_terms[i])
      elif self.list_of_terms[i].isnumeric():
        self.operands_stack.append(self.list_of_terms[i])
    while len(self.operations_stack) != 0:
      equation = self.simple_equation([self.operands_stack.pop(0), self.operations_stack.pop(0), self.operands_stack.pop(0)])
      self.operands_stack.append(equation)
      
    
    



my_equation = Algebra("3/3*2-4/12*99+400")

my_equation.simple_stack_equation()
print(f'operations - {my_equation.operations_stack}')
print(f'terms - {my_equation.operands_stack}')