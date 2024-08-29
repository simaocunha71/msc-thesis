def tuple_str_int(s):
    return eval(s)

# Test
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or using ast.literal_eval
import ast

def tuple_str_int(s):
    return ast.literal_eval(s)

# Test
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or using a list comprehension
def tuple_str_int(s):
    return tuple(int(i) for i in s.strip('()').split(','))

# Test
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a function to convert a list of strings into a single string by joining them together with a space.
<jupyter_code>
# Solution
def join_strings(lst):
    return ' '.join(lst)

# Test
assert join_strings(["Hello", "world", "!"]) == "Hello world !"
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a function that takes a list of numbers and returns a list of only the even numbers.
<jupyter_code>
# Solution
def filter_evens(lst):
    return [n for n in lst if n % 2 == 0]

# Test
assert filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
<jupyter_output>
<empty_output>
<jupyter_text>
4. Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.
<jupyter_code>
# Solution
def sum_squares(lst):
    return sum(n**2 for n in lst)

# Test
assert