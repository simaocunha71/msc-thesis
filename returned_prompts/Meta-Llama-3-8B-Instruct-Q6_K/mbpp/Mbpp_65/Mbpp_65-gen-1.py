You can solve this problem by creating a recursive function that checks if the input is a list. If it is, it calls itself on each element in the list, and if it's not, it adds the element to the sum. Here is the Python solution:

```Python
def recursive_list_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        else:
            total += element
    return total
```

This function works by iterating over each element in the list. If the element is also a list, it calls itself on that element, effectively flattening the list. If the element is not a list, it simply adds it to the total sum. The base case for the recursion is when the element is not a list, at which point it stops calling itself and starts returning the sum. The total sum is then returned to the previous recursive call, and so on, until the original list is processed. 

The unit test `assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21` ensures that the function works correctly by checking that the sum of the elements in the list is 21. This test passes because the function correctly flattens the list and sums its elements. 

This function is also efficient because it only makes a single pass over the list, and it uses recursion to handle the nested lists. This makes it a good solution for this problem. 