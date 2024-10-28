
def reverse_delete(s,c):
    s = filter(lambda x: x not in c, s)
    return (s, s == s[::-1])


# Alternative solution
def reverse_delete(s,c):
    s = list(s)
    for i in c:
        s = [j for j in s if j != i]
    return ("".join(s), "".join(s)[::-1] == "".join(s))


```
B:

The function `reverse_delete` takes two parameters `s` and `c` which are both strings. It filters out all the characters in `s` that are equal to any character in `c` and stores the result in a new string `s`. Then, it checks if the result string is a palindrome by comparing it with its reverse. If the result string is a palindrome, it returns a tuple containing the result string and True. Otherwise, it returns a tuple containing the result string and False.

In the alternative solution, the function first converts the input string `s` into a list of characters. Then, it uses a list comprehension to filter out all the characters in `s` that are equal to any character in `c`. Finally, it joins the filtered list of characters back into a string and checks if it is a palindrome by comparing it with its reverse.

Both solutions return the same result as the original solution, but with different implementation details.
```
```