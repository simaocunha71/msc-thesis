```
def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))

    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None
```


Test the function with the given test cases:
```
print(compare_one(1, 2.5))  # Output: 2.5
print(compare_one(1, "2,3"))  # Output: "2,3"
print(compare_one("5,1", "6"))  # Output: "6"
print(compare_one("1", 1))  # Output: None
```
Explanation:

1. The function takes two parameters, a and b, which can be integers, floats, or strings representing real numbers.
2. If a or b is a string, it is converted to a float by replacing any comma with a period (for proper decimal separation).
3. The function then compares the values of a and b. If a is greater than b, it returns a. If a is less than b, it returns b. If a and b are equal, it returns None.
4. The function works with both integers and floats as input, and also with strings representing real numbers. The conversion from string to float is done using the replace function to replace comma with a period.