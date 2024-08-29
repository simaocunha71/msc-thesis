def remove_nested(tup):
    return tuple(i for i in tup if not isinstance(i, tuple))

print(remove_nested((1, 5, 7, (4, 6), 10)))

#Solution 2:
def remove_nested(tup):
    return tuple(filter(lambda x: not isinstance(x, tuple), tup))

print(remove_nested((1, 5, 7, (4, 6), 10)))

#Solution 3:
def remove_nested(tup):
    return tuple(x for x in tup if type(x)!=tuple)

print(remove_nested((1, 5, 7, (4, 6), 10)))
<jupyter_output>
(1, 5, 7, 10)
(1, 5, 7, 10)
(1, 5, 7, 10)
<jupyter_text>
Q2: Write a Python program to reverse the given string by using slicing method.
<jupyter_code>
def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello, World!"))
<jupyter_output>
<empty_output>
<jupyter_text>
Q3: Write a Python function to generate a dictionary that contains (i, sqrt(i)) for all the numbers from 1 to n (both 1 and n included).
<jupyter_code>
import math

def generate_dict(n):
    return {i: math.sqrt(i) for i in range(1, n+1)}

print(generate_dict(10))
<jupyter_output>
<empty_output>
<jupyter_text>
Q4: Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
<jupyter_code>
def sort_words(s):
    words = s.