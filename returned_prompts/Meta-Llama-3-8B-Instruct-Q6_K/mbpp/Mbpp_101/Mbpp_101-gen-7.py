```
def kth_element(arr, k):
    return arr[k-1]
```


The function `kth_element` takes an array `arr` and an integer `k` as inputs. It returns the `kth` element in the array, using 1-based indexing. The `k-1` is used because Python uses 0-based indexing, so we need to subtract 1 to get the correct index. For example, the first element is at index 0, the second element is at index 1, and so on. The unit test `assert kth_element([12,3,5,7,19], 2) == 3` confirms this. The function works by directly accessing the `kth` element in the array and returning it. It does not sort the array or use any other complex logic, as the problem statement does not require it. Therefore, the function is simple and efficient.