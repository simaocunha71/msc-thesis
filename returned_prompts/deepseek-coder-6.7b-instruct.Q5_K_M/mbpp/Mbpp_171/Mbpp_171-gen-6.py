"""
This problem can be solved using the formula for the perimeter of a pentagon which is 5 times the length of one side.
"""

def perimeter_pentagon(side_length):
    return 5 * side_length

print(perimeter_pentagon(5))  # Should print 25

# Additional Test Cases
print(perimeter_pentagon(10))  # Should print 50
print(perimeter_pentagon(2.5))  # Should print 12.5

# This function should work for any real number input.
# As a result, it may be useful to add some input validation if you expect to handle edge cases.
<jupyter_output>
25
50
12.5
<jupyter_text>
Problem 2
<jupyter_code>
