Here is a possible solution in Java:

```java
public int canArrange(List<Integer> arr) {
    Collections.sort(arr);
    for (int i = 1; i < arr.size(); i++) {
        if (arr.get(i) <= arr.get(i - 1)) {
            return i - 1;
        }
    }
    return -1;
}
```

In this solution, we first sort the array in ascending order. Then we iterate through the array and check if the current element is less than or equal to the previous element. If it is, we return the index of the previous element. If we reach the end of the array without finding such an element, we return -1.

Please note that this solution assumes that the input array will not contain duplicate values. If the input array may contain duplicate values, you should modify the solution accordingly.