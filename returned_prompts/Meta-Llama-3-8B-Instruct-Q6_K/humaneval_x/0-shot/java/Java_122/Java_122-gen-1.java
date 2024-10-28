The problem asks to find the sum of the elements with at most two digits from the first k elements of the given array.

Here is a Java solution for the problem:

```java
public int addElements(List<Integer> arr, int k) {
    int sum = 0;
    for(int i = 0; i < k; i++) {
        if(String.valueOf(arr.get(i)).length() <= 2) {
            sum += arr.get(i);
        }
    }
    return sum;
}
```

In this solution, we iterate over the first k elements of the array. For each element, we convert it to a string and check its length. If the length is less than or equal to 2, it means the element has at most two digits, so we add it to the sum. Finally, we return the sum.

For example, given the array [111,21,3,4000,5,6,7,8,9] and k = 4, the output will be 24, which is the sum of 21 and 3.