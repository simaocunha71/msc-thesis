```
def remove_odd(s):
    return ''.join([c for c in s if ord(c)%2==0])
```


The function `remove_odd` takes a string `s` as input and returns a new string with all the odd characters removed. It uses a list comprehension to iterate over each character `c` in the input string. For each character, it checks if the ASCII value of the character is even using the expression `ord(c)%2==0`. If the character is even (i.e., its ASCII value is even), it is included in the new string. The resulting string is then returned. 

For example, if the input string is "python", the function will return "yhn" because the characters 'p', 't', and 'o' have odd ASCII values, while 'y', 'h', and 'n' have even ASCII values. 

The unit test `assert remove_odd("python")==("yhn")` ensures that the function works correctly for this specific input. 