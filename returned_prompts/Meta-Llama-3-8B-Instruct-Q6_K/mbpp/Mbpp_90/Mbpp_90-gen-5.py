```
def len_log(lst):
    return max(len(word) for word in lst)
```
This function uses a generator expression to calculate the length of each word in the list, and then uses the built-in `max` function to find the maximum length. The unit test `assert len_log(["python","PHP","bigdata"]) == 7` ensures that the function returns the correct result. 

For example, if the input list is `["python","PHP","bigdata"]`, the function will return `7`, which is the length of the longest word "bigdata". 

This function is case-sensitive and considers punctuation as part of the word. If you want to ignore case and punctuation, you can use the `str.lower` and `str.strip` functions, like this:
```
def len_log(lst):
    return max(len(word.strip().lower()) for word in lst)
```
This version of the function will return `7` for the input list `["python","PHP","bigdata"]`, regardless of the case of the words or whether they contain punctuation. 