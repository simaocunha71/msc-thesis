"""
def add_string(list1,format_string):
    return [format_string.format(i) for i in list1]
"""

def add_string(list1,format_string):
    return [format_string.format(i) for i in list1]

def test():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    print("All tests passed.")
test()

# Made By Mostafa_Khaled
```
Here is a simple function to add a string to all elements of a list, using the Python programming language and the format() function. The function takes two arguments: a list and a format string. It then uses a list comprehension to apply the format string to each element in the list, and returns the resulting list. The provided assertion is used to test the function, and prints "All tests passed" if the function works correctly.

In the provided format string, '{0}' is a placeholder that will be replaced by the value of the first argument passed to the format() function. In this case, the first argument is the index of the current element in the list. So, for example, if the original list is [1, 2, 3, 4], the resulting list will be ['temp1', 'temp2', 'temp3', 'temp4'].

The function can be called by passing in a list and a format string as arguments. For example, add_string([1, 2, 3, 4], 'temp{0}') will return ['temp1', 'temp2', 'temp3', 'temp4'].

The provided assertion is used to test the function. If the function works correctly, it will return True and print "All tests passed". Otherwise, it will return False and print an error message.
```