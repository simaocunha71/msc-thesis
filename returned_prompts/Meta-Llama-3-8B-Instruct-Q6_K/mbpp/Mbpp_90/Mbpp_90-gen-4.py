```
def len_log(lst):
    return max(len(x) for x in lst)
```


The function `len_log` takes a list of strings as an argument and returns the length of the longest string in the list. This is achieved by using a generator expression to iterate over the list and calculate the length of each string using the built-in `len` function. The `max` function is then used to find the maximum length.

The unit test `assert len_log(["python","PHP","bigdata"]) == 7` ensures that the function returns the correct result for the given input. The longest string in the list is "bigdata" which has a length of 7. 

This function can be used to find the length of the longest word in a list of words. For example, if you have a list of words like ["hello", "world", "python", "programming"] and you want to find the length of the longest word, you can use the `len_log` function like this: `len_log(["hello", "world", "python", "programming"])`. The function will return the length of the longest word in the list, which is 10 in this case. 