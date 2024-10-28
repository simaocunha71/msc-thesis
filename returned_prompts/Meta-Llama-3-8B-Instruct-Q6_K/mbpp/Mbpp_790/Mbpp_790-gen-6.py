You can use a list comprehension with enumerate to check if every even index contains even numbers. Here is the function:

```
def even_position(lst):
    return all(i % 2 == 0 and isinstance(num, int) and num % 2 == 0 for i, num in enumerate(lst))
```
This function works by iterating over the list with enumerate, which returns both the index and the value. It then checks if the index is even (i % 2 == 0), if the value is an integer (isinstance(num, int)), and if the value is even (num % 2 == 0). The all function then checks if all of these conditions are True, and returns False if any of them are False. 

The unit test `assert even_position([3,2,1]) == False` means that the function should return False for the list [3,2,1] because the first index is even but the number is not even. 

Please note that the function will return False as soon as it finds an index that doesn't meet the condition, so it will stop checking once it finds the first such index. If you want to continue checking even after finding the first index that doesn't meet the condition, you can use any instead of all. 





