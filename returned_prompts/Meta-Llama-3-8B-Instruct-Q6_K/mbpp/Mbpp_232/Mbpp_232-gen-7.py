```
def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]
```
The function `larg_nnum` takes a list `lst` and an integer `n` as inputs. It returns a list containing the `n` largest items from the list. 

The `sorted` function is used to sort the list in descending order (largest to smallest). The `[:n]` slice is used to extract the first `n` items from the sorted list, which are the `n` largest items from the original list.

The unit test `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` ensures that the function returns the correct result. The `set` function is used to remove duplicates and compare the result with the expected output. 

The function works correctly even if there are duplicate values in the list, because the `sorted` function sorts the list based on the values, not the indices. The `set` function is used to remove duplicates in the expected output, but not in the actual output of the function. 

Note that the function returns the `n` largest items from the list, not the `n` largest unique items. If you need to return the `n` largest unique items, you can use a set to remove duplicates before sorting the list. However, this would also remove duplicates from the original list, which might not be the desired behavior. 