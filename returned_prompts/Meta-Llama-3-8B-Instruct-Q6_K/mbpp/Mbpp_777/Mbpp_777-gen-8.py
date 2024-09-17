```
def find_sum(lst):
    return sum(set(lst) - set([x for x in lst if lst.count(x) > 1]))
```


Explanation:
The function `find_sum` takes a list `lst` as input. It first converts the list into a set `set(lst)` to remove duplicates. Then, it converts the list into a list comprehension `[x for x in lst if lst.count(x) > 1]` to get a list of all the elements that appear more than once in the list. The `set` of this list is subtracted from the original set `set(lst)` to get the set of non-repeated elements. Finally, the sum of the non-repeated elements is calculated using the `sum` function. 

The unit test `assert find_sum([1,2,3,1,1,4,5,6]) == 21` checks if the function correctly finds the sum of non-repeated elements in the given list. The expected output is 21, which is the sum of 2, 3, 4, 5, and 6. 

Note: This solution assumes that the input list does not contain duplicate elements. If the input list can contain duplicate elements, the function should return the sum of all elements, not just the non-repeated ones. 

Also, this solution has a time complexity of O(n^2) due to the use of the `count` method inside a list comprehension. This can be improved to O(n) by using a dictionary to count the occurrences of each element. Here is the improved solution:
```
def find_sum(lst):
    count_dict = {}
    for x in lst:
        count_dict[x] = count_dict.get(x, 0) + 1
    return sum(x for x in count_dict if count_dict[x] == 1)
```
This solution uses a dictionary to count the occurrences of each element in the list. Then, it sums up the elements that appear only once in the list. This solution has a time complexity of O(n). 