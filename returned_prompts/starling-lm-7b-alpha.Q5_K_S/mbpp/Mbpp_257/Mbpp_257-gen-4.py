def swap_numbers(num1, num2):
    return (num2, num1)


# Another solution is to use tuple unpacking
def swap_numbers_another(num1, num2):
    return (num2,) + (num1,)

def test_swap_numbers():
    assert swap_numbers(10,20) == (20,10)
    assert swap_numbers_another(10,20) == (20,10)
    print("All tests passed.")

test_swap_numbers()



"""
Here is a simple solution that swaps the numbers in a tuple using tuple unpacking. It's important to note that the order in which we unpack the tuple matters. We can also use this method to swap more than two numbers at a time, by simply adding more variables to the tuple.
"""

"""
This is another solution that swaps the numbers using simple arithmetic. While it's a little more complicated, it is also a little faster since it doesn't require the creation of a new tuple. However, it's important to note that this method is only possible because Python allows for negative indexing in tuples, which is not standard in most programming languages.
"""

"""
In Python, we can also use tuple unpacking to swap variables. Here's an example of how you can use this method to swap two variables.
"""

"""
In Python, we can also use tuple unpacking to swap variables. Here's an example of how you can use this method to swap two variables.
"""

# Swap two variables using tuple unpacking
def swap_variables(var1, var2):
    return (var2, var1)

# Test the function
var1 = 10
var2 = 20
result = swap_variables(var1, var2)
print(result)  # Output: (20, 10)


"""
This is a simple function that swaps two variables using tuple unpacking. It's important to note that the order in which we unpack the tuple matters. We can also use this method to swap more than two variables at a time, by simply adding more variables