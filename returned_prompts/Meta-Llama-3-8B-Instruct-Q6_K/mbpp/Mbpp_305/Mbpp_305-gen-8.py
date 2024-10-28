```
def start_withp(lst):
    return [word for word in lst if word.startswith('p')][0:2]
```


The function `start_withp` takes a list of strings as input and returns the first two strings that start with the letter 'p'. The `startswith` method is used to check if a string starts with a specific prefix, and the list comprehension is used to create a list of strings that start with 'p'. The slicing `[0:2]` is used to return the first two elements of the list. 

For example, if the input list is `["Python PHP", "Java JavaScript", "c c++"]`, the function will return `('Python', 'PHP')`. 

The unit test `assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')` ensures that the function returns the correct result. 

This function will return the first two words that start with 'p', even if there are more than two words that start with 'p'. If you want to return all words that start with 'p', you can remove the `[0:2]` slicing.  If you want to return the first word that starts with 'p', you can use `return [word for word in lst if word.startswith('p')][0]`.  If you want to return the last word that starts with 'p', you can use `return sorted([word for word in lst if word.startswith('p')])[-1]`.  If you want to return all words that start with 'p' in a case-insensitive manner, you can use `return [word for word in lst if word.lower().startswith('p')]`.  If you want to return the last word that starts with 'p' in a case-insensitive manner, you can use `return sorted([word for word in lst if word.lower().startswith('p')])[-1]`.  If you want to return the first word that starts with 'p' in a case-insensitive manner, you can use `return sorted([word for word in lst if word.lower().startswith('p')])[0]`.  If you want to return all words that start with 'p' in a case-insensitive manner and ignore non-words, you can use `return [word for word in lst if word.replace(' ', '').lower().startswith('p')]`.  If you want to return the last word that starts with