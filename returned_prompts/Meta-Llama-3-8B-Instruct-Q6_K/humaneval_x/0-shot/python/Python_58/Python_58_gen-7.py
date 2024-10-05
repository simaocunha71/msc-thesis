```
def common(l1: list, l2: list):
    set1 = set(l1)
    set2 = set(l2)
    return sorted(list(set1 & set2))
```

This function works by first converting the input lists to sets, which are unordered collections of unique elements. The `&` operator is then used to find the intersection of the two sets, which are the elements that are common to both sets. The result is converted back to a list and sorted before being returned. The time complexity of this function is O(n), where n is the total number of elements in the input lists. This is because the conversion of the lists to sets and the finding of the intersection both take O(n) time. The sorting of the result also takes O(n log n) time, but this is dominated by the O(n) time spent on the other operations for large inputs. The space complexity of this function is also O(n), because the sets and the result list all take O(n) space. However, this is a reasonable space complexity for this problem, because the input lists are already taking up O(n) space. 





Here is the output of the test cases:
```
Test case 1:
common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]

Test case 2:
common([5, 3, 2, 8], [3, 2])
[2, 3]
```





The function `common` is a simple and efficient way to find the common elements in two lists. It works by converting the lists to sets, finding the intersection of the sets, and then converting the result back to a list. The function is also able to handle lists of any size, and it returns the common elements in sorted order. The time complexity of the function is O(n), where n is the total number of elements in the input lists, and the space complexity is also O(n), because the function creates a new list to store the result.