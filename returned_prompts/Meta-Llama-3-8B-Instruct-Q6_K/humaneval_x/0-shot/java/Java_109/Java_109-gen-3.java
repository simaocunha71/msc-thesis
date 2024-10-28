The problem is asking to check if it's possible to sort the given array in non-decreasing order by performing right shift operations. 

Here is the solution:

```java
public boolean moveOneBall(List<Integer> arr) {
    int i = 0;
    while (i < arr.size() - 1) {
        if (arr.get(i) > arr.get(i + 1)) {
            return false;
        }
        i++;
    }
    return true;
}
```

The idea is to iterate through the array and check if the current element is greater than the next element. If it is, then it's not possible to sort the array by performing right shift operations, so we return false. If we finish the iteration without finding any such pair, it means the array can be sorted by performing right shift operations, so we return true. 

Note that we only need to check until the second last element, because the last element can be moved to the front by a right shift operation, so we don't need to check it. 

This solution has a time complexity of O(n), where n is the size of the array, because we only need to iterate through the array once. 

Also, note that this solution assumes that the input array is not null and has at least one element. If the input array can be empty, we should add a special case to handle this. For example:

```java
public boolean moveOneBall(List<Integer> arr) {
    if (arr.isEmpty()) {
        return true;
    }
    int i = 0;
    while (i < arr.size() - 1) {
        if (arr.get(i) > arr.get(i + 1)) {
            return false;
        }
        i++;
    }
    return true;
}
```

This solution will return true for an empty array, which is a valid result according to the problem statement. 