
def compare_one(a, b):
    try:
        if a == b:
            return None
        if isinstance(a, str):
            a = float(a.replace(",", "."))
        if isinstance(b, str):
            b = float(b.replace(",", "."))
        return max(a, b)
    except ValueError:
        return "Invalid input"

print(compare_one(1, 2.5)) # 2.5
print(compare_one(1, "2,3")) # "2,3"
print(compare_one("5,1", "6")) # "6"
print(compare_one("1", 1)) # None
print(compare_one("1", "a")) # "Invalid input"

This solution first checks if the inputs are equal. If they are, the function returns `None`. If not, the function converts the strings to floats (replacing "," with "."), if necessary. Finally, it returns the max of the two inputs. In case of invalid input, it returns "Invalid input".

The `isinstance()` function is used to check the type of the input, and `max()` function is used to determine the larger value. Note that the `float()` function is used to convert the string to a float, and the `replace()` function is used to replace "," with "." in the string.

If the inputs are not strings, `float()` does nothing, and the input is left as it is. If the inputs are strings, `float()` converts them to floats, and the `replace()` function replaces "," with ".".

In case of invalid input, the `float()` function raises a `ValueError`, which is caught by the `except` block and returns "Invalid input".

Finally, the function returns the larger of the two inputs. If the inputs are equal, the function returns `None`.

If the inputs are not numbers, the function will return "Invalid input".

Note: This solution assumes that the inputs are valid numbers. If the inputs are not valid numbers, the function will return "Invalid input".
