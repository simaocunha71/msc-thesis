```
def extract_rear(tup):
    return [s[-1] for s in tup]
```


The function `extract_rear` takes a tuple `tup` as input. It uses a list comprehension to iterate over each string `s` in the tuple. For each string, it uses Python's indexing feature to access the last character of the string (`s[-1]`). The list comprehension collects these last characters into a new list, which is then returned. The unit test `assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']` ensures that the function works correctly. 

Note that this function assumes that each string in the tuple has at least one character. If a string might be empty, you would need to add error checking code to handle this case. 

Also, Python uses zero-based indexing, so the last character of a string is at index `-1`. The `-1` is a special index in Python that always refers to the last element of a sequence. 

The function `extract_rear` is case sensitive and will return the last character of each string as it is. If you want to make it case insensitive, you can convert each string to lower case or upper case before extracting the last character. For example, you can use `s[-1].lower()` to get the last character of each string in lower case. 