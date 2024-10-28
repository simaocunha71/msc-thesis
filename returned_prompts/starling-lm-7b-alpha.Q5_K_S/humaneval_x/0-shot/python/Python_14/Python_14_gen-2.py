    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i + 1])
    return prefixes


# These "asserts" using only for self-checking and not necessary
# for auto-testing
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("*** Test Suite Passed ***")
```
In this program, the `all_prefixes` function takes a string as input and returns a list of all prefixes of the input string, from shortest to longest. 

To achieve this, the function initializes an empty list called `prefixes`. Then, it uses a `for` loop to iterate over the range of the length of the input string. Inside the loop, it appends each prefix of the input string to the `prefixes` list using slicing. Finally, the function returns the `prefixes` list.

In the provided test case, the `all_prefixes` function is called with the string `'abc'`. The expected output is `['a', 'ab', 'abc']`, which represents the shortest to longest prefixes of the input string. 

The `doctest` module is imported to perform self-checking of the code. If all assertions pass, the program prints "*** Test Suite Passed ***".

Overall, this program provides a solution to generate a list of all prefixes of a given string from shortest to longest.

Note: The `doctest` module is used for self-checking purposes and is not necessary for the correct functioning of the code.

```python
def all_prefixes(string: str) -> List[str]:
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i + 1])
    return prefixes
```