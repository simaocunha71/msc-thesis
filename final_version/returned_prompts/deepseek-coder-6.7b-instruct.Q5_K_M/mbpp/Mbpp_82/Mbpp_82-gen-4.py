def volume_sphere(radius):
    return 4/3 * math.pi * radius**3

print(volume_sphere(10))
<jupyter_output>
4188.790204786582
<jupyter_text>
Q2: Write a Python function to solve the quadratic equation ax^2 + bx + c = 0. The function should return the two roots as a tuple. The roots should be calculated using the quadratic formula, `x = [-b ± sqrt(b^2 - 4ac)] / 2a`.
<jupyter_code>
import math

def solve_quadratic(a, b, c):
    root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return (root1, root2)

print(solve_quadratic(1, -3, 2))  # Example usage
<jupyter_output>
(2.0, 1.0)
<jupyter_text>
Q3: Write a Python function that accepts a string and returns a dictionary with the count of each character in the string. The function should be case-insensitive.
<jupyter_code>
def char_count(s):
    s = s.lower()
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

print(char_count("Hello, World!"))  # Example usage
<jupyter_output>
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, 'j': 1}
<jupyter_text>
Q4: Write a Python function that checks whether a given string is a palind