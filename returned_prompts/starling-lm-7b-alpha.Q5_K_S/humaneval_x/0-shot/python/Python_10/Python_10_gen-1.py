
Here is a Python function that tests if a given string is a palindrome, and a function to find the shortest palindrome that begins with a supplied string.

The idea behind the `make_palindrome` function is quite simple. We start by finding the longest postfix of the supplied string that is a palindrome. We then append to the end of the string the reverse of the prefix that comes before the palindromic suffix.

The `is_palindrome` function checks if a string is a palindrome. It does this by comparing the string to its reverse. If the two are the same, then the string is a palindrome.

The `make_palindrome` function first checks if the supplied string is already a palindrome. If it is, it returns the string. If not, it finds the longest palindromic suffix by repeatedly checking if the string is a palindrome. It keeps track of the longest suffix it finds. Once it finds the longest suffix, it checks if the prefix of the string before the suffix is a palindrome. If it is, it appends the reverse of the prefix to the end of the string and returns the result. If the prefix isn't a palindrome, the function appends the reverse of the prefix, slices the string to remove the prefix, and calls itself again to find the next longest palindrome.

The `make_palindrome` function uses a while loop to repeat this process until it finds the shortest palindrome that begins with the supplied string.

Here are a few examples of how to use these functions:

```python
print(is_palindrome('racecar'))  # Returns True
print(is_palindrome('hello'))  # Returns False
print(make_palindrome(''))  # Returns ''
print(make_palindrome('cat'))  # Returns 'catac'
print(make_palindrome('cata'))  # Returns 'catac'
```

These functions should give you a good starting point for finding the shortest palindrome that begins with a supplied string.

The time complexity of `is_palindrome` function is O(n/2) where n is the length of the string. This is because we only need to compare half the string to its reverse