def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += (2*i)**2
    return sum

print(square_Sum(2))

# Output: 20

# Test case 2
assert square_Sum(3) == 50

# Test case 3
assert square_Sum(4) == 120

# Test case 4
assert square_Sum(5) == 250

# Test case 5
assert square_Sum(6) == 400

# Test case 6
assert square_Sum(7) == 570

# Test case 7
assert square_Sum(8) == 760

# Test case 8
assert square_Sum(9) == 970

# Test case 9
assert square_Sum(10) == 1200
<jupyter_output>
20
<jupyter_text>
Question 2: Write a python function that takes a string str and returns a string made of the middle character of the input string. If the length of the string is even, the function should return the middle two characters.
<jupyter_code>
# Answer:

def middle_char(str):
    length = len(str)
    if length % 2 == 0:
        return str[length//2-1:length//2+1]
    else:
        return str[length//2]

# Test case 1
assert middle_char('abc') == 'b'

# Test case 2
assert middle_char('abcd') == 'bc'

# Test case 3
assert middle_char('abcde') == 'c'

# Test case 4
assert middle_char('abcdef') == 'cd'
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3: Write a Python function that takes a list of numbers and returns a list of only the even numbers.
<jupyter_code>
# Answer:

def filter_even(lst):
    return [num for num in lst if