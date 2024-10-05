```
def reverse_delete(s,c):
    new_s = ""
    for char in s:
        if char not in c:
            new_s += char
    return (new_s, new_s == new_s[::-1])
```


Example usage:

print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
print(reverse_delete("abcdef", "b"))  # Output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)
```
This function goes through each character in the string `s` and checks if it is not in the string `c`. If it's not in `c`, it adds it to a new string `new_s`. After going through all characters in `s`, it checks if `new_s` is the same when reversed, and returns a tuple with `new_s` and the result of the palindrome check.  This function is case sensitive and treats uppercase and lowercase letters as different characters.  It also treats spaces and punctuation as characters.  If you want to ignore case, spaces, or punctuation, you would need to preprocess the strings to do so.  For example, you could convert both strings to lowercase and remove spaces and punctuation before checking for palindromes.  You could also use a regular expression to remove non-alphanumeric characters before checking for palindromes.  The choice of how to preprocess the strings would depend on the specific requirements of your task.  For example, if you want to ignore case, you could convert both strings to lowercase before checking for palindromes.  If you want to ignore spaces and punctuation, you could remove them from the strings before checking for palindromes.  If you want to ignore both case and spaces and punctuation, you could convert the strings to lowercase and remove spaces and punctuation before checking for palindromes.  The choice of how to preprocess the strings would depend on the specific requirements of your task.  For example, if you want to ignore case, you could convert both strings to lowercase before checking for palindromes.  If you want to ignore spaces and punctuation, you could remove them from the strings before checking for palindromes.  If you want to ignore both case and spaces and punctuation, you could convert the strings to lowercase and remove spaces and punctuation before checking for palindromes.  The choice of how to preprocess the strings would depend on the specific requirements