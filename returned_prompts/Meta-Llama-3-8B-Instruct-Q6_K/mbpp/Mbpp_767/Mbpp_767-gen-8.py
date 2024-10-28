```
def get_pairs_count(lst, sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count
```
This function iterates over the list and checks each pair of elements to see if their sum equals the given sum. If it does, it increments the count. The time complexity of this solution is O(n^2) because for each element in the list, it checks the rest of the list.

You can also use dictionary to store the frequency of each number and then use this dictionary to count the number of pairs whose sum is equal to the given sum. This will reduce the time complexity to O(n). Here is the code:

```
def get_pairs_count(lst, sum):
    freq = {}
    count = 0
    for num in lst:
        if sum - num in freq:
            count += freq[sum - num]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return count
```
This function first creates a dictionary where the keys are the numbers in the list and the values are their frequencies. Then it iterates over the list again and for each number, it checks if the number that would make the sum equal to the given sum is in the dictionary. If it is, it adds the frequency of that number to the count. Finally, it returns the count. This solution is more efficient than the previous one for large lists. 