```
def get_positive(l: list):
    return [num for num in l if num > 0]
```


Explanation:
The function `get_positive` takes a list `l` as an argument. It uses a list comprehension to iterate over each number in the list. If the number is greater than 0 (i.e., positive), it is included in the new list. The function then returns this new list.

The unit tests provided demonstrate the function's behavior with different inputs. The function correctly filters out non-positive numbers and returns only the positive numbers in the list.