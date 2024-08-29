
def sum_square(lst):
    return sum([i**2 for i in lst])

print(sum_square([1, 2, 3, 4, 5]))
assert sum_square([1, 2, 3, 4, 5]) == 55
<jupyter_output>
55
<jupyter_text>
Q4:Write a Python function that takes a list of strings and returns the longest string. If there are multiple strings of the same longest length, return the first one.assert longest_string(["hello", "world", "python", "is", "awesome"]) == "awesome"
<jupyter_code>
