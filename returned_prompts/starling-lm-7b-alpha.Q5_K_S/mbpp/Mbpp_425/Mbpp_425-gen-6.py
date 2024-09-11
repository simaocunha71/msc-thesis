```
def count_element_in_list(list1,element):
    count=0
    for i in list1:
        if element in i:
            count+=1
    return count
```

Explanation:

In this code, the function `count_element_in_list` takes in two parameters: `list1` (the list of sublists) and `element` (the element to be counted). 

The function initializes a variable `count` to 0, which will keep track of the number of sublists containing the element. 

Then, it iterates through each sublist `i` in the `list1`. For each sublist, it checks if the `element` is present using the `in` operator. If it is, the `count` is incremented by 1. 

After iterating through all the sublists, the function returns the final count. 

In the given assertion, the function `count_element_in_list` is called with the list `[[1, 3], [5, 7], [1, 11], [1, 15, 7]]` and the element `1`. The expected result is 3, as there are three sublists containing the element `1` (`[1, 3]`, `[1, 11]`, and `[1, 15, 7]`). 

The function correctly counts the occurrence of the element and returns the correct result, satisfying the assertion.

It's important to note that this solution assumes that the sublists are nested lists, and not tuples or other data structures.

Additionally, the function does not consider the order of elements within the sublists, only their presence. If the order matters, a different approach would be needed.

Lastly, it's worth mentioning that the function could be optimized by using a different data structure or algorithm, but for simplicity and readability, this solution is sufficient.

Overall, this function provides a straightforward and effective way to count the number of sublists containing a particular element in a given list of sublists.

Note: It's important to note that the provided solution assumes that the input list `list1` is a valid Python list of lists (i.e.,