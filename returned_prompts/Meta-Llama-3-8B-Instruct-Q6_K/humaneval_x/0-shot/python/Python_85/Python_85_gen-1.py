```
def add(lst):
    return sum(i for i in lst if i % 2 == 0 and lst.index(i) % 2 != 0)
```


Explanation:
The function add(lst) iterates over the list lst. It checks each element i in the list to see if it's even (i % 2 == 0) and if it's at an odd index (lst.index(i) % 2 != 0). If both conditions are met, it adds the element to the sum. The sum of all these elements is then returned. This function only considers the even elements at odd indices, as required by the problem statement. 

Please note that this function will not work correctly if the list contains duplicate elements, because the index() function will always return the index of the first occurrence of the element. If you need to handle duplicate elements, you should use a list comprehension to filter the list before summing its elements. 

Here's how you can modify the function to handle duplicate elements:

```
def add(lst):
    return sum(i for i in set(i for i in lst if i % 2 == 0 and lst.index(i) % 2 != 0))
```


In this modified function, the set() function is used to remove duplicate elements before summing them. This ensures that each element is only added to the sum once, even if it appears multiple times in the list. 