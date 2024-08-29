def dog_age(human_age):
    return human_age * 7

print(dog_age(12))

# Output: 84
# Explanation: A dog's age in dog's years is the human age multiplied by 7. So, 12 human years is equivalent to 84 dog years.
<jupyter_output>
84
<jupyter_text>
12. Write a function to calculate the area of a circle given its radius. The area of a circle is given by the formula πr².
<jupyter_code>
import math

def circle_area(radius):
    return math.pi * radius ** 2

print(circle_area(5))

# Output: 78.53981633974483
# Explanation: The area of the circle is given by the formula πr². Here r is 5, so the area of the circle is π*(5^2) = 78.53981633974483.
<jupyter_output>
78.53981633974483
<jupyter_text>
13. Write a function that takes a string and returns a new string with all the vowels removed.
<jupyter_code>
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in string if char not in vowels])

print(remove_vowels('Hello, World!'))

# Output: 'Hll, Wrld!'
# Explanation: The vowels in the string 'Hello, World!' are 'e', 'o', 'a', 'o', 'o', 'u'. The new string with the vowels removed is 'Hll, Wrld!'
<jupyter_output>
Hll, Wrld
<jupyter_text>
14. Write a function that takes a string and returns a new string with all the characters reversed.
<jupyter_code>
def reverse_string(string):
