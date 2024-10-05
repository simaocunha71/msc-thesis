The problem is asking to find the minimum sum of any non-empty sub-array of a given array of integers. 

Here is a simple solution in Java:

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

This solution initializes two variables, `minSum` and `currentSum`, to keep track of the minimum sum and the sum of the current sub-array respectively. It then iterates over the array, adding each number to `currentSum` and updating `minSum` if `currentSum` is smaller. If `currentSum` becomes greater than 0, it resets `currentSum` to 0 to start a new sub-array. 

At the end of the iteration, `minSum` will hold the minimum sum of any non-empty sub-array. 

The time complexity of this solution is O(n), where n is the size of the input array, because it needs to iterate over the array once. The space complexity is O(1), because it only uses a constant amount of space to store the two variables. 

This solution assumes that the input array is not empty. If the input array can be empty, you should add a check at the beginning of the method to return 0 in that case. 

For example:

```java
public int minSubArraySum(List<Integer> nums) {
    if (nums.isEmpty()) {
        return 0;
    }

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