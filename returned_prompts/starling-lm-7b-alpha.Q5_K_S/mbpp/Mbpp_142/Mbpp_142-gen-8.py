```
def count_samepair(list1,list2,list3):
    count = 0
    for i in range(len(list1)):
        if(list1[i]==list2[i]==list3[i]):
            count+=1
    return count
```

In this function, we're going to check each item in the first list against the second and third. If all three lists have the same item at the same index, we increase the count by one. 

To check if all three lists have the same item at the same index, we use a series of equal-to comparisons. If the item in `list1` at index `i` is equal to the item in `list2` at index `i` and is equal to the item in `list3` at index `i`, we increment the `count` variable by one. 

Finally, we return the `count` variable, which represents the number of items that are identical in the same position of three given lists. 

For the given test case `count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])`, the function will return `3`, as there are three identical items in the same position of the three given lists. 

This is the correct solution to your problem.

Here is the step-by-step reasoning behind this solution:

1. Initialize a variable `count` to 0. This variable will keep track of the number of identical items in the same position of the three given lists.
2. Use a `for` loop to iterate through each item in the first list.
3. Inside the loop, check if the item in `list1` at index `i` is equal to the item in `list2` at index `i` and is equal to the item in `list3` at index `i`. If all three conditions are true, increment the `count` variable by one.
4. After the loop, return the `count` variable, which represents the number of identical items in the same position of the three given lists.
5. For the given test case `count_samepair([