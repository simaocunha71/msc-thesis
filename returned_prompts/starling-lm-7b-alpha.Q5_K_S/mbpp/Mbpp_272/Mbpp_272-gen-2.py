```
def rear_extract(list_of_tuples):
    return [tup[-1] for tup in list_of_tuples]
```

Explanation:
The `rear_extract` function takes in a list of tuples as its input. It uses a list comprehension to iterate over each tuple in the list and extract the last element (i.e., the rear element) of each tuple. The resulting list of rear elements is then returned by the function. 

In the given example, `rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)])` is called, which returns `[21, 20, 19]`. This means that the rear element of the first tuple (21), the rear element of the second tuple (20), and the rear element of the third tuple (19) have been extracted and returned in a new list. 

Overall, the function is able to successfully extract the rear elements of each tuple in the input list and return a new list containing only those rear elements.

The time complexity of this function is O(n), where n is the number of tuples in the input list. This is because the function needs to iterate over each tuple in the list once to extract the rear element. The space complexity is also O(n) as the function creates a new list to store the extracted rear elements.

Here's a breakdown of the code:
- The function `rear_extract` takes in a parameter `list_of_tuples`, which is the input list of tuples.
- The function uses a list comprehension to iterate over each tuple `tup` in the `list_of_tuples`. For each tuple, it extracts the last element (i.e., the rear element) using `tup[-1]`.
- The extracted rear elements are collected in a new list, which is then returned by the function.
- The function is tested with the provided example, and the expected output is obtained. 

Overall, the function is able to successfully extract the rear elements of each tuple in the input list and return a new list containing only those rear elements.

The time complexity of this function is O(