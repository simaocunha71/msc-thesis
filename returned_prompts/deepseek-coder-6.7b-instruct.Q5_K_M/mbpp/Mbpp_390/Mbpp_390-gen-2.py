def add_string(lst, string):
    return [string.format(i) for i in lst]

print(add_string([1,2,3,4],'temp{0}'))

# Output: ['temp1', 'temp2', 'temp3', 'temp4']

"""
This function works by using a list comprehension to iterate through each element in the list. It applies the format string to each element using the str.format() method and returns a new list with the modified elements.
"""

