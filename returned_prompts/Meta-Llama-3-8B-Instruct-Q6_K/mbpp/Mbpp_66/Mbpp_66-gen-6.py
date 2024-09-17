You can use the built-in sum function and a generator expression to count the number of positive numbers in a list. Here is how you can do it:

```Python
def pos_count(lst):
    return sum(1 for x in lst if x > 0)
```
This function works by iterating over each element in the list, and for each element, it checks if it is greater than 0. If it is, it adds 1 to the total count. The sum function then adds up all these 1s to give the total count of positive numbers in the list.

For example, if you run pos_count([1,-2,3,-4]), it will return 2 because there are two positive numbers in the list. This is in accordance with the unit test provided, which asserts that pos_count([1,-2,3,-4]) should return 2. 