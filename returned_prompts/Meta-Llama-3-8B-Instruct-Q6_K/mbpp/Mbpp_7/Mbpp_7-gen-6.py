```
def find_char_long(s):
    words = s.split()
    char_long = [word for word in words if len(word) >= 4]
    return set(char_long)
```


This function works by first splitting the input string into a list of words using the `split` method. It then uses a list comprehension to create a new list that only includes the words that are at least 4 characters long. Finally, it converts this list to a set (which removes duplicates) and returns it. The unit test provided ensures that the function works correctly. 

For example, if the input is 'Please move back to stream', the function will return {'Please', 'move', 'back', 'stream'}, which are all the words in the input string that are at least 4 characters long. 

The `assert` statement in the unit test checks that the function returns the expected result. 

The time complexity of this function is O(n), where n is the number of words in the input string. This is because the function iterates over each word in the input string once. The space complexity is also O(n), as the function creates a new list and set that can potentially contain the same number of words as the input string. 







