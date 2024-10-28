Here is the solution for the problem:

```java
public int addElements(List<Integer> arr, int k) {
    int sum = 0;
    for (int i = 0; i < k && i < arr.size(); i++) {
        int num = arr.get(i);
        if (String.valueOf(num).length() <= 2) {
            sum += num;
        }
    }
    return sum;
}
```

Explanation:

*   We iterate through the first `k` elements of the array.
*   For each element, we convert it to a string and check its length. If the length is less than or equal to 2, it means the number has at most two digits.
*   We add the number to the sum if it has at most two digits.
*   Finally, we return the sum.

This solution has a time complexity of O(k), where `k` is the input parameter, and a space complexity of O(1), as we only use a constant amount of space to store the sum.