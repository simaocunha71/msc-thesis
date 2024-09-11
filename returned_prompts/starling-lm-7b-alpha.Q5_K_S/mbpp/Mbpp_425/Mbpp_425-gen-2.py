```
def count_element_in_list(list, element):
    count = 0
    for sublist in list:
        if element in sublist:
            count += 1
    return count
```

Explanation:

The function `count_element_in_list` takes in two parameters: `list` and `element`. It initializes a variable `count` to 0, which will keep track of the number of sublists containing the specified element. 

Next, a `for` loop is used to iterate over each sublist in the input `list`. For each sublist, it checks if the specified `element` is present in the sublist using the `in` operator. If the element is found, the `count` variable is incremented by 1. 

Finally, the function returns the total count of sublists containing the specified element.

The provided `assert` statement verifies that the function returns the correct result for the given test case, where the input `list` is `[[1, 3], [5, 7], [1, 11], [1, 15, 7]]` and the element to search for is 1. 

By executing the `count_element_in_list` function with the provided input, it will return 3, indicating that there are three sublists in the input list that contain the element 1.

Overall, this solution provides a simple and efficient way to count the number of sublists containing a specific element in a nested list.































































































```

```