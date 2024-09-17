```
def get_pairs_count(lst, sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count
```
Explanation:
This function iterates over the list and checks each pair of numbers to see if their sum equals the given sum. The count of such pairs is returned. In the given unit test, the function should return 6 because there are 6 pairs of numbers in the list [1,1,1,1] that sum up to 2. The function is not case sensitive and will treat numbers as integers. For example, it will treat 1 and 1 as the same number, not as two different numbers. 

This function has a time complexity of O(n^2) where n is the length of the list because it needs to iterate over the list for each element. This might not be efficient for large lists. If you need a more efficient solution, you can use a hash map to store the numbers you've seen so far and their counts, which would reduce the time complexity to O(n). 

Here is the more efficient version of the function:
```
def get_pairs_count(lst, sum):
    count = 0
    seen = {}
    for num in lst:
        complement = sum - num
        if complement in seen:
            count += seen[complement]
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    return count
```
This function has a time complexity of O(n) where n is the length of the list. It iterates over the list once and uses a hash map to store the numbers it has seen. For each number, it checks if its complement (the number that would make the sum equal to the given sum) is in the hash map. If it is, it adds the count of that number to the total count. Then it increments the count of the current number in the hash map. This way, it keeps track of the numbers it has seen and their counts, which allows it to find the pairs in a single pass over the list. 














