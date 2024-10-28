```
def len_log(words):
    return max(len(word) for word in words)
```
This function uses a generator expression to iterate over each word in the input list, calculates the length of each word using the built-in `len` function, and then uses the built-in `max` function to find the maximum length. The result is the length of the longest word in the list. The unit test `assert len_log(["python","PHP","bigdata"]) == 7` ensures that the function returns the correct result for the given input. 