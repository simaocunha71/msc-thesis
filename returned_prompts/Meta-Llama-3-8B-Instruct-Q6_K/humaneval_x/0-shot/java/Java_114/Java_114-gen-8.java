The problem is asking to find the minimum sum of any non-empty sub-array of a given array of integers. 

Here is the solution in Java:

```java
public int minSubArraySum(List<Integer> nums) {
    int minSum = Integer.MAX_VALUE;
    int currentSum = 0;
    for (int num : nums) {
        currentSum += num;
        minSum = Math.min(minSum, currentSum);
        if (currentSum > 0) {
            currentSum = 0;
        }
    }
    return minSum;
}
```

This solution initializes two variables, `minSum` and `currentSum`, to keep track of the minimum sum and the sum of the current sub-array respectively. It then iterates over the given array, adding each number to `currentSum` and updating `minSum` if `currentSum` becomes smaller. If `currentSum` becomes positive, it resets `currentSum` to 0. Finally, it returns `minSum`, which is the minimum sum of any non-empty sub-array. 

This solution has a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1), as it only uses a constant amount of space to store the variables. 

You can test this function with the examples you provided:

```java
System.out.println(minSubArraySum(Arrays.asList(2, 3, 4, 1, 2, 4))); // Output: 1
System.out.println(minSubArraySum(Arrays.asList(-1, -2, -3))); // Output: -6
```  