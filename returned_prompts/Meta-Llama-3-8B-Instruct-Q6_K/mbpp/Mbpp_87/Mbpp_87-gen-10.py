```
def merge_dictionaries_three(dict1, dict2, dict3):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = value
    for key, value in dict3.items():
        if key in result:
            if result[key] != value:
                raise ValueError(f"Key {key} has different values in dictionaries")
        else:
            result[key] = value
    return result
```


The function `merge_dictionaries_three` takes three dictionaries as input and returns a new dictionary that combines the key-value pairs from all three dictionaries. If there are any duplicate keys, the function will raise a `ValueError` if the values for those keys are different. If you want to overwrite the values from the first dictionary with the values from the other dictionaries, you can simply use the `update` method of the dictionary. Here is the code:

```
def merge_dictionaries_three(dict1, dict2, dict3):
    result = dict1.copy()
    result.update(dict2)
    result.update(dict3)
    return result
```
This code will work as long as the values for duplicate keys are the same. If the values for duplicate keys are different, you will need to decide which value to keep. The first version of the function I provided will raise an error if the values for duplicate keys are different. If you want to keep the value from the first dictionary, you can modify the function as follows:

```
def merge_dictionaries_three(dict1, dict2, dict3):
    result = dict1.copy()
    result.update(dict2)
    result.update(dict3)
    return result
```


This function will overwrite the values from the first dictionary with the values from the other dictionaries. If you want to keep the values from the first dictionary, you can modify the function as follows:

```
def merge_dictionaries_three(dict1, dict2, dict3):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = value
    for key, value in dict3.items():
        if key in result:
            if result[key] != value:
                raise ValueError(f"Key {key} has different values in dictionaries")
        else:
            result[key] = value
    return result
```
This function will keep the values from the first dictionary if they are different from the values in the other dictionaries. If you want to keep the values from the other dictionaries, you