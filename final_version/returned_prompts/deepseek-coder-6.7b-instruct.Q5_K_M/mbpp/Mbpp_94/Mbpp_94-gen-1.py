
def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]

print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))
<jupyter_output>
Varsha
<jupyter_text>
Problem 2: Write a Python program that takes a list of integers and a target value, and determines the two integers in the list that sum closest to the target value. Return these two integers as a tuple. If there are multiple pairs of integers that sum to the same closest value, return the first one you find.
<jupyter_code>
