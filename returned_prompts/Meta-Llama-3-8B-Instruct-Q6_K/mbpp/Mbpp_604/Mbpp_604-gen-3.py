def reverse_words(s):
    return ' '.join(s.split()[::-1])

# Test the function
print(reverse_words("python program"))  # Output: "program python"  # Test the function
print(reverse_words("Hello World"))  # Output: "World Hello"  # Test the function
print(reverse_words("This is a test"))  # Output: "test a is This"  # Test the function
print(reverse_words("Reverse function"))  # Output: "function Reverse"  # Test the function
print(reverse_words("Reverse words separated by spaces"))  # Output: "spaces by separated words Reverse"  # Test the function
print(reverse_words("Reverse words"))  # Output: "words Reverse"  # Test the function
print(reverse_words("Reverse"))  # Output: "Reverse"  # Test the function
print(reverse_words(""))  # Output: ""  # Test the function

# The function works by splitting the string into words using the split() function, 
# reversing the list of words using slicing with a step of -1, 
# and then joining the reversed list of words back into a string using the join() function. 
# The join() function concatenates the elements of the list (in this case, the reversed words) 
# into a single string, using the string passed as the first argument (in this case, a space) 
# as the separator between the elements. 
# For example, if the input string is "hello world", 
# the function will split it into the list ["hello", "world"], 
# reverse the list to get ["world", "hello"], 
# and then join the reversed list back into the string "world hello". 
# The function works correctly even if the input string is empty, 
# in which case it returns an empty string. 
# The function also works correctly if the input string contains leading or trailing spaces, 
# or if it contains multiple spaces between the words, 
# because the split() function and the join() function ignore these spaces. 
# The function is case-sensitive, so it will reverse the words in the original order of their first appearances in the string. 
# The function is also locale-dependent, so it may not work correctly if the input string contains non-ASCII characters. 
# However, for most purposes, the function should work correctly and efficiently.  # Test the function
# The function has a time complexity of O(n), 
#