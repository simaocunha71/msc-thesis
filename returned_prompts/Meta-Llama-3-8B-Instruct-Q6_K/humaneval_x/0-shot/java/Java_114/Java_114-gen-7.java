The problem is asking you to find the minimum sum of any non-empty sub-array of the given array. 

Here is the Java solution for this problem:

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

This solution iterates through the array and keeps track of the sum of the current sub-array. It also keeps track of the minimum sum found so far. If the sum of the current sub-array becomes positive, it resets the sum to 0. This way, it ensures that it considers all possible sub-arrays and finds the minimum sum. 

For example, if the input array is [2, 3, 4, 1, 2, 4], the minimum sum of any non-empty sub-array is 1 (which is the sum of the sub-array [1]). If the input array is [-1, -2, -3], the minimum sum of any non-empty sub-array is -6 (which is the sum of the sub-array [-1, -2, -3]). 

This solution has a time complexity of O(n), where n is the size of the input array, because it iterates through the array once. The space complexity is O(1), because it uses a constant amount of space to store the minimum sum and the current sum. 