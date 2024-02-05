from sympy import symbols, sqrt, simplify, expand, I

# Define the variable x
x = symbols('x')

# Define the expression
expression = (((x + sqrt(x**2 + 4))**I - (x - sqrt(x**2 + 4))**I) / (2**I * sqrt(x**2 + 4)))

# Calculate and print the expression for i from 0 to 20
for i in range(21):
    result = expand(expression.subs(I, i))
    print(f"For i = {i}: {result}")