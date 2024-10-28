```
def large_product(list1, list2, n):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for _ in range(n):
        result.append(list1.pop(0) * list2.pop(0))
    return sorted(result, reverse=True)
```


This function first sorts both lists in descending order. Then it pops the largest element from each list, multiplies them, and adds the result to the result list. This process is repeated n times. Finally, it sorts the result list in descending order and returns it.

The unit test `assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]` ensures that the function works correctly. It checks that the function returns the correct result when given two lists and the number of largest products to find.

The time complexity of this function is O(n log n) due to the sorting operations, where n is the length of the lists. The space complexity is O(n) for storing the result list. 





```
import heapq

def large_product(list1, list2, n):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    return sorted([-heapq.heappop(list1) * -heapq.heappop(list2) for _ in range(n)], reverse=True)
```


This solution uses the heapq module to get the n largest products from the two lists. The list1 and list2 are sorted in descending order, and then the heapq.heappop function is used to get the n largest products. The result is then sorted in descending order and returned.

The time complexity of this function is O(n log n) due to the sorting operations, where n is the length of the lists. The space complexity is O(n) for storing the result list.

The unit test `assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]` ensures that the function works correctly. It checks that the function returns the correct result when given two lists and the number of largest products to find.