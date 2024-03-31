import sympy 
from sympy import symbols 
from sympy.solvers import solve 

x = symbols('x') 

# Put the equation here
eq = 3*(7*x) + 22*(1/3)

print("x = ", solve(eq,x))