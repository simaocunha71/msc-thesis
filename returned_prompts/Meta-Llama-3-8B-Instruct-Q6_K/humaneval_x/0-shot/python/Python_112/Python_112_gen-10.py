```
def reverse_delete(s,c):
    # convert s and c to sets for faster lookup
    s_set = set(s)
    c_set = set(c)
    
    # remove characters from s that are in c
    result = ''.join([char for char in s if char not in c_set])
    
    # check if the result is palindrome
    is_palindrome = result == result[::-1]
    
    return (result, is_palindrome)
```


Explanation:
We convert both strings s and c to sets for faster lookup. Then we create a new string result by joining all characters in s that are not in c. Finally, we check if the result is a palindrome by comparing it with its reverse. If they are the same, then it's a palindrome. We return a tuple containing the result string and a boolean indicating whether it's a palindrome.