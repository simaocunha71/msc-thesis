Here is a Python solution for the problem:

```Python
def exchange(lst1, lst2):
    lst1 = list(lst1)
    lst2 = list(lst2)
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    if odd_count <= len(lst2):
        return "YES"
    else:
        return "NO"
```
This solution works by first converting the input lists to actual lists (as they are input as iterables). It then counts the number of odd numbers in `lst1`. If this count is less than or equal to the length of `lst2`, it is possible to exchange elements from `lst2` to make all the elements of `lst1` even, so the function returns "YES". Otherwise, it returns "NO". 

The reason why it checks if the count of odd numbers in `lst1` is less than or equal to the length of `lst2` is that for each odd number in `lst1`, we can replace it with an even number from `lst2`. So, if there are more odd numbers in `lst1` than even numbers in `lst2`, it is not possible to make all the elements of `lst1` even by exchanging elements with `lst2`. 

This solution assumes that the input lists will be non-empty, as specified in the problem description. It also assumes that the input lists will only contain numbers, as specified in the problem description. If the input lists could contain non-numeric values, additional error checking would be needed. 