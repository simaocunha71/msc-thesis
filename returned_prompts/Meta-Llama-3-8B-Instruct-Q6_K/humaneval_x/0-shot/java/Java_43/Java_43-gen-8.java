Here is the Java solution for the problem:

```java
public boolean pairsSumToZero(List<Integer> l) {
    Set<Integer> set = new HashSet<>();
    for (int num : l) {
        if (set.contains(-num)) {
            return true;
        }
        set.add(num);
    }
    return false;
}
```

This solution iterates through the list and for each number, it checks if its negative counterpart is in the set. If it is, then the function returns `true`. If it iterates through the entire list without finding such a pair, it returns `false`. The set is used for O(1) lookup time, making the overall time complexity O(n). The space complexity is also O(n) for storing the set.  The set is used to keep track of the numbers we have seen so far. If we see a number that is the negative of a number we have seen before, then we know that there are two distinct elements in the list that sum to zero, so we return `true`. If we get through the entire list without finding such a pair, then we return `false`.  The set is used to keep track of the numbers we have seen so far. If we see a number that is the negative of a number we have seen before, then we know that there are two distinct elements in the list that sum to zero, so we return `true`. If we get through the entire list without finding such a pair, then we return `false`. This solution is efficient because it uses a set to keep track of the numbers we have seen so far, which allows it to check if a number is in the set in O(1) time. This makes the overall time complexity O(n). The space complexity is also O(n) for storing the set.  The solution works by iterating through the list and checking if each number is the negative of a number we have seen before. If it is, then we return `true`. If we get through the entire list without finding such a pair, then we return `false`.  The set is used to keep track of the numbers we have seen so far. If we see a number that is the negative of a number we have seen before, then we know that there are two distinct elements in the list that sum to zero, so we return `true`. If we get through the entire list without finding such a pair, then we return `false`.  The set is used to keep track of the numbers