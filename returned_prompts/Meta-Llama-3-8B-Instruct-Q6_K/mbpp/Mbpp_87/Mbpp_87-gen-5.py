```
def merge_dictionaries_three(dict1, dict2, dict3):
    result = {}
    result.update(dict1)
    result.update(dict2)
    result.update(dict3)
    return result
```
This function takes three dictionaries as input and returns a new dictionary that contains all the key-value pairs from the three input dictionaries. If there are any duplicate keys, the value from the last dictionary to be updated will be used. 

For example, in the unit test provided, the key "W" appears in both the second and third dictionaries, and the value "White" is used from the third dictionary. 

The function uses the update method of the dictionary to merge the dictionaries. This method updates the dictionary with the key-value pairs from the input dictionary. If a key already exists in the dictionary, its value will be updated. 

The function returns the merged dictionary. 

Here's how you can use this function:
```
dict1 = {"R": "Red", "B": "Black", "P": "Pink"}
dict2 = {"G": "Green", "W": "White"}
dict3 = {"O": "Orange", "W": "White", "B": "Black"}

result = merge_dictionaries_three(dict1, dict2, dict3)
print(result)
``` 
This will print:
```
{'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
```  # output
```
This is the expected output because it contains all the key-value pairs from the three input dictionaries. If there are any duplicate keys, the value from the last dictionary to be updated is used. 

Note that this function does not raise an error if there are duplicate keys. If you want to raise an error in such cases, you can modify the function to use the `dict.setdefault` method instead of the `dict.update` method. The `dict.setdefault` method sets a default value for a key if it does not already exist in the dictionary. If the key does already exist, it simply returns the value for that key. This can be useful if you want to avoid overwriting values in the dictionary. 

Here's how you can modify the function to use the `dict.setdefault` method:
```
def merge_dictionaries_three(dict1, dict2, dict3):
    result = {}
    for key, value in dict1.items():
        result.setdefault(key,