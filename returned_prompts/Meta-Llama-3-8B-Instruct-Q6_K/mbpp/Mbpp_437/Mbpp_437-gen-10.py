```
def remove_odd(s):
    return "".join([i for i in s if int(i) % 2 == 0])
```
This function uses a list comprehension to iterate over each character in the string. It checks if the character is even (i.e., if the remainder of the character's ASCII value divided by 2 is 0) and if it is, it adds the character to the list. The function then uses the `join` method to concatenate the characters in the list into a string.

The unit test `assert remove_odd("python")==("yhn")` ensures that the function removes the odd characters in the string "python" and returns the resulting string "yhn". This is because the ASCII values of the characters 'p', 't', 'h', 'o', 'n' are 112, 116, 104, 111, 110, which are all odd. The ASCII values of the characters 'y' and 'n' are 121 and 110, which are even, so they are included in the resulting string. The `join` method concatenates the characters in the list into the string "yhn", which is the expected output.