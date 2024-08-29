def empty_list(n):
    return [{} for _ in range(n)]
"""
Testing the function:
"""
assert empty_list(5)==[{},{},{},{},{}]
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:Write a Python function that accepts a list of dictionaries where each dictionary represents a student and has two keys: 'name' and 'grade'. The function should return a new dictionary where the keys are the student names and the values are their respective grades.
<jupyter_code>
