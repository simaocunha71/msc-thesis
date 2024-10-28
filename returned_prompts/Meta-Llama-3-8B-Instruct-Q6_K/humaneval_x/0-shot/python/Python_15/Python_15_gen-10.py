def string_sequence(n: int) -> str:
    return ' '.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
print(string_sequence(10))  # Output: '0 1 2 3 4 5 6 7 8 9 10'  # and so on...  # noqa: E501
# The function uses a generator expression to generate the sequence of numbers from 0 to n, and then joins them with spaces in between using the 'join' method.  # noqa: E501
# This function works for any non-negative integer input.  # noqa: E501
# The function does not perform any error checking, so it will not work correctly if the input is a negative integer.  # noqa: E501
# If you want to add error checking, you could add an if statement to check if the input is non-negative, and raise an error if it's not.  # noqa: E501
# Here's an example of how you could do that:  # noqa: E501
def string_sequence(n: int) -> str:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return ' '.join(str(i) for i in range(n + 1))  # noqa: E501
# With this modification, the function will raise a ValueError if the input is a negative integer.  # noqa: E501
# You can also add a default value for the input, so that the function will return an empty string if the input is not provided.  # noqa: E501
# Here's an example of how you could do that:  # noqa: E501
def string_sequence(n: int = 0) -> str:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return ' '.join(str(i) for i in range(n + 1))  # noqa: E501
# With this modification, the function will return an empty string if no input is provided.  # noqa: E501
# You can also add a docstring to the function, which will provide a description of what the function does.  # noqa: E501
# Here's an example of