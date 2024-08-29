def sum_length_of_names(names):
    return sum(len(name) for name in names if not name[0].islower())

print(sum_length_of_names(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))


"""
The function sum_length_of_names takes a list of names as its argument. It uses a generator expression to iterate over the list of names. 
For each name in the list, it checks if the first character of the name is a lowercase letter using the islower method. If the first character is not a lowercase letter, it adds the length of the name to the sum. 
Finally, it returns the sum of the lengths of the names that passed the condition.
"""

"""
Another way to solve this problem is to use the built-in filter function to create a new list of names that start with an uppercase letter. 
Then, you can use the sum function to add up the lengths of the names in the new list. Here is the Python code for this approach:
"""

def sum_length_of_names(names):
    upper_names = filter(lambda name: name[0].isupper(), names)
    return sum(len(name) for name in upper_names)

print(sum_length_of_names(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))


"""
In this code, the filter function is used to create a new list of names that start with an uppercase letter. 
The lambda function is used to define the condition for filtering. The sum function is then used to add up the lengths of the names in the new list.
"""
<jupyter_output>
16
<jupyter_text>
