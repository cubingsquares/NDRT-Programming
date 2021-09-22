# This program solves the quadratic equation
# 
# Name: Jack Kalicak
# Date: 19 September 2021
# Python with Pat Week 1 Challenge 1

# one solution: 2, 3, 1.125
# complex solution: 1,2,3
import math
import cmath

a = float(input('a value: '))
b = float(input('b value: '))
c =float(input('c value: '))


test = b**2 - 4*a*c

if a != 0:
    if test > 1:
        root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        print('')
        print('Roots: ' + str(root1) + ' using plus,' + str(root2) +' using minus')
    elif test == 0:
        root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a) 
        print('Root: ' + str(root1))
    else:
        root1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
        root2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
        print('')
        print('Roots: ' + str(root1) + ' using plus,' + str(root2) +' using minus')
else:
    print('This is not a quadratic equation')

