```
def new_tuple(string_list, string):
    return tuple([*string_list, string])
```
This function takes two parameters: a list and a string. It uses the unpacking operator `*` to expand the list into separate arguments to the `tuple` function, and then appends the string as the third argument. The result is a new tuple that combines the elements of the list and the string.

The unit test `assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')` confirms that the function works correctly. It checks that the output of the function is a tuple containing the elements "WEB", "is", and "best" in that order. The function passes this test, so it is correct.