```
def interleave_lists(list1, list2, list3):
    return [x for t in zip(list1, list2, list3) for x in t]
```
This function uses the built-in Python `zip` function to pair up the elements of the three input lists. The list comprehension then flattens these pairs into a single list. 

For example, if you call `interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])`, the function will return the list `[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]`. 

The unit test provided in the problem ensures that the function works correctly for lists of length 7. However, the function will also work for lists of any length, as long as they are the same length. If the lists are not the same length, the function will stop at the end of the shortest list.  For example, `interleave_lists([1,2,3],[10,20,30,40],[100,200,300])` will return `[1, 10, 100, 2, 20, 200, 3, 30]`. 

This function is case-insensitive, meaning it will work the same whether the input lists contain integers, strings, or any other type of object. However, it does assume that the input lists are iterable and that they contain the same number of elements. If these assumptions are not met, the function may not work correctly.  For example, if you call `interleave_lists([1,2,3],[4,5],[6])`, the function will raise a `TypeError` because the input lists are not the same length.  Similarly, if you call `interleave_lists('abc','def','ghi')`, the function will raise a `TypeError` because the input lists contain strings, not integers.  To avoid these errors, you can add error checking code to the function to handle these cases.  For example, you could add a check to make sure the input lists are the same length, and raise an error if they are not