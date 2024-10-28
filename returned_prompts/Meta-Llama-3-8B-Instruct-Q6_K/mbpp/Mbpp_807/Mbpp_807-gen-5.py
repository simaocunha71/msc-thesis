```
def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
    return None
```
This function iterates over the list of numbers and returns the first number that is odd (i.e., not divisible by 2). If no odd number is found, it returns None. The unit test `assert first_odd([1,3,5]) == 1` ensures that the function correctly identifies the first odd number in the list.