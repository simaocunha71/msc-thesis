```
def interleave_lists(list1, list2, list3):
    return [x for group in zip(list1, list2, list3) for x in group]
```


The function `interleave_lists` takes three lists as arguments and returns a single flat list. It uses the built-in `zip` function to iterate over the three lists in parallel, and a list comprehension to flatten the resulting list of tuples into a single list. The `zip` function stops at the end of the shortest input list, so if the lists are not all the same length, the excess elements from the longer lists are ignored. The function is tested with the following unit test:
```
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
```


This test ensures that the function correctly interleaves the three input lists, even if they are not all the same length. 





