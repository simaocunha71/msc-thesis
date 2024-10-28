```
def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
    return None
```
This function iterates over the list of numbers. If it finds a number that is not divisible by 2 (i.e., an odd number), it returns that number. If it doesn't find any odd numbers in the list, it returns None.

The unit test `assert first_odd([1,3,5]) == 1` ensures that the function returns the first odd number in the list, which is 1 in this case. If the function didn't return 1, the test would fail. 

Note: This function assumes that the input list is not empty. If the list could be empty, you might want to add a check for that and return None or a special value in that case. 

Also, the function will return the first odd number it finds. If there are multiple odd numbers in the list, this function will return the first one. If you want to return all odd numbers in the list, you would need a different approach. 