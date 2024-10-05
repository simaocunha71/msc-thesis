    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False


# These "asserts" using `assert `${condition}` `# ${ok}` are helping
# to get an overview, they are only used for the doctests or if
# option `--doctest-modules` is given.

# Note: `# ${ok}` will not be shown in the test results, only the `.` or `X`
# on the left side

assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

# The above `assert` statements are defined for doctests, but can be run in a python console normally.

# The `from __future__ import division` is a special line at the top of the file
# that allows for `1 / 2 == 0.5` instead of `1 / 2 == 1` which can be counter intuitive.

# If you are using python3, you can remove the line and the division will work as expected.

# The `__name__` check is a common python idiom to prevent a function or method from being run directly
# when a module is imported. It is a way to protect the `__name__` variable from being accessed directly.

# The `__name__` of a module is the name of the package it was imported under. When the module is run directly
# like `python3 __main__.py`, `__name__` is set to `__main__`. When the module is imported like `from module import *`,
# `__name__` is set to the name of the package it was imported under.

# Here is a sample run of this script



if __name__ == "__main__":
    print("All tests passed")

```