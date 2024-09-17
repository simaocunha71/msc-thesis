```
def start_withp(words):
    result = [word.split()[0] for word in words if word.startswith('p')]
    return tuple(result)
```
This function takes a list of words as input and returns a tuple of two words that start with 'p'. It uses a list comprehension to iterate over the list of words, split each word into a list of words (assuming the list of words is a string), and checks if the first word in the list starts with 'p'. If it does, it adds the word to the result list. Finally, it converts the result list to a tuple and returns it.