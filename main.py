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


my_equation = Algebra("x+x-y=z")

print(my_equation.list_of_terms)