
    return ' '.join(str(i) for i in range(n+1))


if __name__ == "____main__":
    import doctest
    doctest.testmod()


# The function uses a generator expression to create a sequence of numbers from 0 to n inclusive.
# The join method is then used to convert the sequence into a string, with each number separated by a space.

# This function can be tested using the doctest module by calling doctest.testmod().
# This function will check the docstring comments for any examples given and verify that the function's output matches the expected output.

# If the function's output matches the expected output for all examples given, the function will pass the tests.
# If the function's output does not match the expected output for any example, the function will raise an AssertionError and the tests will fail.

# This allows for a simple way to test the function and ensure that it's working as expected.

# To run the tests, simply call the function with no arguments. If the function is correct, it will not output anything.
# If the function is incorrect, it will output a message indicating that the tests failed.

# This is a simple example of how to use doctest to test a function. It allows you to write tests directly in the docstring comments, making it easy to see what the function should do and how it should behave.
# It also provides a simple way to run the tests and see if the function is working as expected.

# This is a bit of a simplification, but it's a start. There are many other features and options available with doctest, such as running tests in a specific order, ignoring certain tests, and more.
# Check out the doctest documentation for more information.
<jupyter_output>
<empty_output>
<jupyter_text>
7. Write a Python program to reverse the given string.
<jupyter_code>
def reverse_string(s: str) -> str:
    """ Return the reversed string.
    >>> reverse_string('hello')
    'olleh'
    >>> reverse_string('Python')
    'nohtyP'
    """
