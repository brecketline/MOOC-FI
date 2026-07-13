# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt
valuea = int(input('Value of a: '))
valueb = int(input('Value of b: '))
valuec = int(input('Value of c: '))

root1 = (- valueb + sqrt((valueb ** 2) - 4 * valuea * valuec)) / (valuea * 2)
root2 = (- valueb - sqrt((valueb ** 2) - 4 * valuea * valuec)) / (valuea * 2)

print(f'The roots are {root1} and {root2}')


# Note that the square
# root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
