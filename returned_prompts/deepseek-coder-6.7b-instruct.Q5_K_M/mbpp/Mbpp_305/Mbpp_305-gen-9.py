def is_palindrome(word):
    return word == word[::-1]

def palindromes(words):
    return [word for word in words if is_palindrome(word)]

print(palindromes(['madam', 'python', 'radar', 'level', 'hello']))

# Output: ['madam', 'radar', 'level']

# This code works by first defining a helper function, is_palindrome, that checks if a word is the same forwards and backwards.

# It then defines the main function, palindromes, which uses a list comprehension to iterate over the input list of words. For each word, it checks if it's a palindrome and if it is, it adds it to the new list.

# Finally, it prints the list of palindromes.
<jupyter_