```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(min(len(list1), len(list2), len(list3))):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
```


The function `count_samepair` takes three lists as input and returns the count of items that are identical in the same position of the three lists. It iterates over the minimum length of the three lists to avoid `IndexError`. If the items at the same position in all three lists are identical, it increments the count. Finally, it returns the count. The unit test `assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3` ensures that the function works correctly. 

This solution is efficient because it only iterates over the minimum length of the three lists, which reduces the number of iterations. It also checks for identical items at the same position in all three lists, which ensures the correctness of the count. The function is simple and easy to understand, making it a good solution for the problem. 





