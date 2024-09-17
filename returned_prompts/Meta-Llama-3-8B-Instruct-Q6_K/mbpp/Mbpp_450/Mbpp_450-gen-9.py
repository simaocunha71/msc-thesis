```
def extract_string(lst, size):
    return [s for s in lst if len(s) >= size]
```
This function takes a list of strings and a size as input, and returns a new list containing only the strings from the original list that have a length of at least the specified size. 

For example, if you call `extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)`, it will return `['practice', 'solution']` because these are the only strings in the list that have a length of at least 8 characters. 

The unit test `assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']` ensures that the function behaves as expected. 

This solution uses a list comprehension, which is a concise way to create a new list in Python. The comprehension iterates over the input list, checks if the length of each string is greater than or equal to the specified size, and includes the string in the new list if the condition is true. 

The time complexity of this function is O(n), where n is the length of the input list, because it needs to iterate over the entire list to check the length of each string. The space complexity is O(m), where m is the number of strings in the output list, because that's the maximum amount of space needed to store the output. 





