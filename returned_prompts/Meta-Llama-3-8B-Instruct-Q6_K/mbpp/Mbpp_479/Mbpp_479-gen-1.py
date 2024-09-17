You can solve this problem by using the built-in function int() to convert the number into a string, then use a loop to find the first digit. Here is the python function:

```Python
def first_Digit(n):
    s = str(n)
    for i in range(len(s)):
        if s[i].isdigit():
            return int(s[i])
```

The unit test `assert first_Digit(123) == 1` ensures that the function returns the correct result for the given input. This function works by converting the number into a string, then iterating over the string to find the first digit. It returns the first digit as an integer.

Please note that this function will return the first digit from the left, not the right. For example, for the input 123, it will return 1, not 3. If you want to return the first digit from the right, you can modify the function to start the loop from the end of the string:

```Python
def first_Digit(n):
    s = str(n)[::-1]
    for i in range(len(s)):
        if s[i].isdigit():
            return int(s[i])
```  This function will return the first digit from the right. For example, for the input 123, it will return 3. 