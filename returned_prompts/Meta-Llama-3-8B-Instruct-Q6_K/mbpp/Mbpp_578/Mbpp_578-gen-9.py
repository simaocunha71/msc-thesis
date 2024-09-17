```
def interleave_lists(list1, list2, list3):
    return [x for t in zip(list1, list2, list3) for x in t]
```



The function `interleave_lists` takes three lists as input and returns a single flat list where elements from the three input lists are interleaved. The `zip` function is used to group the elements from the three lists into tuples, and then a list comprehension is used to flatten these tuples into a single list.

The unit test provided in the problem statement is used to verify the correctness of the function. It checks if the function returns the expected interleaved list when given three lists of the same length. The expected output is a list where the elements from the three input lists are interleaved, and this is verified by comparing the output of the function with the expected output.

Here is an example of how to use the function:
```
list1 = [1,2,3,4,5,6,7]
list2 = [10,20,30,40,50,60,70]
list3 = [100,200,300,400,500,600,700]

result = interleave_lists(list1, list2, list3)
print(result)  # Output: [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
```



This function is efficient and easy to use, and it can be used to interleave any number of lists of the same length. It is also flexible, as it can handle lists of different lengths by ignoring any extra elements in the longer lists. For example, if the lists have different lengths, the function will stop interleaving when the shortest list is exhausted. This is useful if you want to interleave lists of different lengths, or if you want to handle lists with missing values.