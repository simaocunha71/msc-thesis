def tuple_modulo(t1, t2):
    return tuple(map(lambda x, y: x % y, t1, t2))

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))

"""
Output:
(0, 4, 5, 1)
"""

Explanation:

We use the built-in `map` function to apply a lambda function to each pair of elements from the two tuples. The lambda function takes two arguments and returns their modulus. The result is a new tuple.
"""

# Python Programming/Python_Basics/Functions/2_default_arguments.py
"""
Default Arguments:
------------------
We can provide a default value to a function argument. This way, the function will use that default value as a fallback if the function is called without providing the argument.
"""

def greet(name="World"):
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))

"""
Output:
Hello, World
Hello, Alice
"""

Explanation:

We have a function `greet` that takes one argument `name`. If no argument is provided when we call `greet`, it uses the default value "World". If an argument is provided, it uses that value instead.
"""

# Python Programming/Python_Basics/Functions/3_keyword_arguments.py
"""
Keyword Arguments:
------------------
We can also pass arguments to a function using keyword arguments. This is useful when we want to specify the values of certain arguments without worrying about their order.
"""

def greet(name="World", greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet(name="Alice"))
print(greet(greeting="Hi", name="Bob"))

"""
Output:
Hello, Alice
Hi, Bob
"""

Explanptyion:

In this example, `greet` function takes two arguments `name` and `greeting`. We call `g