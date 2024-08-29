
def surfacearea_cube(side_length):
    return 6 * side_length ** 2

print(surfacearea_cube(5))

# Output: 150
<jupyter_output>
150
<jupyter_text>
Q2: Write a function to solve the quadratic equation ax^2 + bx + c = 0. The function should take in three numbers a, b, and c and return a tuple of the solutions.
<jupyter_code>
#Ans:
import cmath

def solve_quadratic(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b - discriminant) / (2 * a)
    root2 = (-b + discriminant) / (2 * a)
    return (root1, root2)

print(solve_quadratic(1, -3, 2))

# Output: (1.0, 2.0)
<jupyter_output>
(1.0, 2.0)
<jupyter_text>
Q3: Write a function that takes in a list of numbers and returns the mean (average) of the numbers.
<jupyter_code>
#Ans:
def mean(numbers):
    return sum(numbers) / len(numbers)

print(mean([1, 2, 3, 4, 5]))

# Output: 3.0
<jupyter_output>
3.0
<jupyter_text>
Q4: Write a function to check if a number is even or odd. The function should return True if the number is even and False if the number is odd.
<jupyter_code>
#Ans:
def is_even(number):
    return number % 2 == 0

print(is_even(4))

# Output: True
<jupyter_output>
True
<jupyter_text>
Q5: Write a function that takes in a string and returns the number of vowels in the string.