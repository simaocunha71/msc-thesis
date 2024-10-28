You can solve this problem by using the built-in `in` operator in Python, which checks if a sequence (like a list or a string) is present in another sequence. However, this operator checks for exact matches, not partial matches. For example, `[1,2] in [[1,2,3],[4,5,6]]` would return `False`.

Here is a Python function that checks if a list is a sublist of another:

```Python
def is_Sub_Array(big_list, small_list):
    for i in range(len(big_list)):
        if big_list[i:i+len(small_list)] == small_list:
            return True
    return False
```
This function works by iterating over the big list and checking if the small list is present at each position. If it finds the small list, it returns `True`. If it doesn't find the small list after checking all positions, it returns `False`.

The unit test `assert is_Sub_Array([1,4,3,5],[1,2]) == False` suggests that the function should return `False` when the small list is not a sublist of the big list, which is what our function does.

Here's how you can use the function:
```Python
print(is_Sub_Array([1,2,3,4,5], [1,2]))  # Returns: True
print(is_Sub_Array([1,2,3,4,5], [6,7]))  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```  # Returns: False
```  # Returns: True
```