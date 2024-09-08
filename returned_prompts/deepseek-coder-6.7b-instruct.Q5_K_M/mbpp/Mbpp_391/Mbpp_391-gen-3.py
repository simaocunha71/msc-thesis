"""
def convert_list_dictionary(keys, values1, values2):
    return [{keys[i]: {values1[i]: values2[i]}} for i in range(len(keys))]

print(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],[85, 98, 89, 92]))
"""

# Output:
"""
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""

# Explanation:
"""
The function takes three lists as inputs. It creates a dictionary with the first list as keys and the second list as values. Then it creates a nested dictionary with the third list as values. Finally, it returns a list of these dictionaries.
"""
<jupyter_output>
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
<jupyter_text>
Question 3
<jupyter_code>
# Question:
"""
Write a function that takes in a list of integers and returns the largest product that can be obtained by multiplying any three integers.

assert max_product([-10, -10, 1, 3, 2])==100
assert max_product([-4, -4, 2, 8])==128
assert max_product([1, 2, 3, 4, -5])==-6
assert max_product([-10, 2, 3, 4, 5])==60
assert max_product([-10, 0, 3, 