def string_sequence(n: int) -> str:
    return ' '.join(map(str, range(n + 1)))  # ' '.join() is used to concatenate all the numbers with a space in between
# Test cases
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
# The function works by using the map() function to convert a range of numbers (from 0 to n) into a list of strings
# Then, ' '.join() is used to concatenate all these strings with a space in between to form the final output string. 
# The range() function is used to generate a sequence of numbers from 0 to n. 
# The map() function is used to convert these numbers into strings. 
# The ' '.join() function is used to concatenate these strings with a space in between.  # Output: 0 1 2 3 4 5 6 7 8 9 10
# The function works by using the map() function to convert a range of numbers (from 0 to n) into a list of strings
# Then, ' '.join() is used to concatenate all these strings with a space in between to form the final output string. 
# The range() function is used to generate a sequence of numbers from 0 to n. 
# The map() function is used to convert these numbers into strings. 
# The ' '.join() function is used to concatenate these strings with a space in between.  # Output: 0 1 2 3 4 5 6 7 8 9 10
# The function works by using the map() function to convert a range of numbers (from 0 to n) into a list of strings
# Then, ' '.join() is used to concatenate all these strings with a space in between to form the final output string. 
# The range() function is used to generate a sequence of numbers from 0 to n. 
# The map() function is used to convert these numbers into strings. 
# The ' '.join() function is used to concatenate these strings with a space in between.  # Output: 0 1 2 3