```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
```


Explanation:
The function `is_happy(s)` checks if a given string `s` is happy or not. 
A string is happy if its length is at least 3 and every 3 consecutive letters are distinct. 
The function does this by first checking if the length of the string is less than 3. 
If it is, the function returns `False` because a string with a length less than 3 cannot be happy. 
Next, the function iterates over the string, checking every 3 consecutive letters to see if they are distinct. 
If it finds a set of 3 consecutive letters that are not distinct, it returns `False` because the string is not happy. 
If the function iterates over the entire string without finding any sets of 3 consecutive letters that are not distinct, it returns `True` because the string is happy. 
The function uses the `or` operator to check if any of the 3 consecutive letters are the same, and the `==` operator to check if two letters are the same. 
The function also uses the `range` function to generate a sequence of indices to iterate over the string. 
The function returns `False` if the string is not happy and `True` if the string is happy. 
This function can be used to check if a given string is happy or not. 
For example, `is_happy("abcd")` would return `True` because every 3 consecutive letters in the string are distinct. 
Similarly, `is_happy("aabb")` would return `False` because the letters 'a' and 'b' are not distinct. 
The function is flexible and can be used to check if any string is happy or not. 
It is also efficient because it only needs to iterate over the string once to check if it is happy. 
This makes it a good solution for this problem. 
The function can be used in a variety of applications where it is necessary to check if a string is happy or not. 
For example, it could be used in a program that generates random strings and checks if they are happy or