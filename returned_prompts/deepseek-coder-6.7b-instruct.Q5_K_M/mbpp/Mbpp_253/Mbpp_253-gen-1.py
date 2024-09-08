
def count_integer(lst):
    return len([i for i in lst if type(i) == int])

print(count_integer([1,2,'abc',1.2]))  # 2

# The function is counting the number of elements in the list that have the type int. It does this by iterating over the elements in the list and checking their type with the built-in function type(). If the type of the element is int, it is added to the new list. The function then returns the length of this new list.

# The assert statement is used to test the function. It checks if the result of the function is equal to 2. If it is, the test passes. If not, the test fails and an error will be raised.
<jupyter_output>
2
<jupyter_text>
Problem 2
<jupyter_code>
