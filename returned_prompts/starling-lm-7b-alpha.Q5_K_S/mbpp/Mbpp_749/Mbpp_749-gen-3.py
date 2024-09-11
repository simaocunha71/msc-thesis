def sort_numeric_strings(strings):
    return sorted(strings, key=int)


# Manual Test Cases
print(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']))
print(sort_numeric_strings(['100', '200', '300', '400', '500']))
print(sort_numeric_strings(['-300', '-200', '-100', '-500']))
print(sort_numeric_strings(['-10', '-5', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))


# Assertion Test Cases
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
assert sort_numeric_strings( ['100', '200', '300', '400', '500'])==[-500, -200, -100, 0, 100, 200, 300, 400, 500]
assert sort_numeric_strings( ['-300', '-200', '-100', '-500'])==[-500, -300, -200, -100]
assert sort_numeric_strings( ['-10', '-5', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])==[-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Time Complexity: O(n log n)
# Space Complexity: O(n)

"""
In the above solution, we have used built-in Python function sorted