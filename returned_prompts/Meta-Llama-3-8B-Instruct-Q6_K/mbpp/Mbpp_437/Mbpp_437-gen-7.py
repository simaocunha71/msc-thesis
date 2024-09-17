```
def remove_odd(s):
    return "".join([i for i in s if int(i)%2==0])
```
The function takes a string as an argument and returns a new string with all the odd characters removed. It does this by iterating over each character in the string, checking if the character is even (i.e., if its integer value is even), and if so, adding it to the new string.

The unit test `assert remove_odd("python")==("yhn")` helps to clarify the problem by providing an example of the expected output for a given input. In this case, the expected output is `"yhn"`, which is the string `"python"` with all the odd characters removed.

The solution uses a list comprehension to create a new list containing only the even characters, and then joins this list into a string using the `join` method. The `int(i)%2==0` condition checks if the integer value of the character is even, and if so, includes the character in the new string. Otherwise, it is skipped. The resulting string is the one with all the odd characters removed. 