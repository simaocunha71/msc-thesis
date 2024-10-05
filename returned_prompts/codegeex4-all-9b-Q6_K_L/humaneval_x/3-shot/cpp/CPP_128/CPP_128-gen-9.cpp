
The has_close_elements function looks ok to me.  Just a couple of things I'd point out:
First, don't use a single letter variable name.  It's hard to tell what i and j represent.
Second, you could use a more descriptive name for the function.  What does "numbers" represent?  How about "values"?
Third, it's good practice to have a comment describing what the function does.  You can do this with a docstring.
Fourth, you might want to consider handling the case of an empty vector.  In your function, if the vector is empty, the function will return false.
Fifth, I'd suggest initializing the values of i and j to 0 before the for loops.  This is a good practice because you don't want to have to worry about what the values are when you use them.
Sixth, you could use the std::abs function to calculate the absolute value.  This makes the code more readable.
Here's a version of the function with some of these suggestions implemented:
def has_close_elements(values, threshold):
    """
    Check if in given vector of numbers, are any two numbers closer to each other than given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(values) == 0:
        return False

    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            if abs(values[i] - values[j]) < threshold:
                return True

    return False

The separate_paren_groups function looks ok to me, but I'd suggest adding a docstring to describe what the function does.  Also, you might want to consider handling the case of an empty string.  In your function, if the string is empty, the function will return an