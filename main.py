def parse_equation(equation):
  equation = [char for char in equation]
  parsed_equation = []
  operations = "+-*/="
  left = 0

  while left < len(equation):
    right = left
    if equation[left] in operations:
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
  
  def add(self, index_1, index_2):
    return int(self.list_of_terms[index_1]) + int(self.list_of_terms[index_2])
  
  def subtract(self, index_1, index_2):
    return int(self.list_of_terms[index_1]) - int(self.list_of_terms[index_2])
  
  def multiply(self, index_1, index_2):
    return int(self.list_of_terms[index_1]) * int(self.list_of_terms[index_2])

  def divide(self, index_1, index_2):
    return int(self.list_of_terms[index_1]) / int(self.list_of_terms[index_2])
  
  def simple_equation(self, indices):
    if self.list_of_terms[indices[1]] == "+":
      return self.add(indices[0], indices[2])
    if self.list_of_terms[indices[1]] == "-":
      return self.subtract(indices[0], indices[2])
    if self.list_of_terms[indices[1]] == "*":
      return self.multiply(indices[0], indices[2])
    if self.list_of_terms[indices[1]] == "/":
      return self.divide(indices[0], indices[2])


my_equation = Algebra("3/3=x")

print(my_equation.simple_equation([0, 1, 2]))