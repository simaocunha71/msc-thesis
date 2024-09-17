```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
```    
This function iterates over the three lists simultaneously using their indices. If the elements at the same index in all three lists are equal, it increments the count. Finally, it returns the total count of identical elements in the same position. The provided unit test `assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3` verifies that the function works correctly. It checks that the function returns `3` for the given input lists. If the function is correct, it should return `3` for this test case.