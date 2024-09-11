```
def get_pairs_count(num_list,sum):
    count = 0
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if(num_list[i]+num_list[j] == sum):
                count += 1
    return count

print(get_pairs_count([1,1,1,1],2))
```

Explanation:
In this question we need to count the number of pairs of numbers whose sum is equal to a given sum. The function get_pairs_count takes two parameters, num_list which is a list of integers and sum which is an integer. We initialize a variable count to 0 to keep track of the count of pairs. We use two nested loops to iterate over each element in the num_list. The outer loop iterates from the first element to the second to last element and the inner loop iterates from the next element to the last element. We check if the sum of the current element in the outer loop and the element in the inner loop is equal to the given sum. If it is, we increment the count by 1. After the loops finish, we return the count.

The time complexity of this solution is O(n^2) because we have two nested loops that iterate over the num_list. The space complexity is O(1) because we only use a constant amount of extra space to keep track of the count.

For example, when we call get_pairs_count([1,1,1,1],2), it will return 6 because there are 6 pairs of numbers that sum up to 2 in the given list.

```python
def get_pairs_count(num_list,sum):
    count = 0
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if(num_list[i]+num_list[j] == sum):
                count += 1
    return count

print(get_pairs_count([1,1,1,1],2)) # Output: 6
```

In this example, we call the function get_pairs_