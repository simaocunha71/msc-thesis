Here is the solution to the problem:

```java
public boolean pairsSumToZero(List<Integer> l) {
    Set<Integer> set = new HashSet<>();
    for (Integer num : l) {
        if (set.contains(-num)) {
            return true;
        }
        set.add(num);
    }
    return false;
}
```

Explanation:

*   We create a HashSet `set` to store the elements of the input list `l`.
*   We iterate through each element `num` in the list.
*   For each element, we check if its negative counterpart is present in the `set` using the `contains` method. If it is, we return `true` because we have found a pair that sums to zero.
*   If we don't find a pair that sums to zero, we add the current element to the `set` and continue the iteration.
*   If we reach the end of the iteration without finding a pair that sums to zero, we return `false`.

This solution has a time complexity of O(n), where n is the size of the input list, because we make a single pass through the list. The space complexity is O(n) as well, because we store all the elements of the list in the `set`.