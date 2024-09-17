```
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict
```
This function uses the dictionary unpacking feature of Python to merge the three input dictionaries into a single dictionary. The `**` operator is used to unpack the dictionaries and combine them into a new dictionary. The resulting dictionary contains all the key-value pairs from the three input dictionaries.

The unit test provided ensures that the function works correctly by asserting that the output of the function is a dictionary that contains all the key-value pairs from the input dictionaries. The test case checks that the resulting dictionary does not contain any duplicate keys and that the values for each key are correct.