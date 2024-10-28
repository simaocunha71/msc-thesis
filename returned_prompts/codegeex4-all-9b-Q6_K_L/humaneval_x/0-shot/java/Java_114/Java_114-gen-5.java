```java
public int minSubArraySum(List<Integer> nums) {
    int res = Integer.MAX_VALUE;
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums.get(i);
        res = Math.min(res, sum);
        if (sum > 0) sum = 0;
    }
    return res;
}
```

Explanation:
We use a sliding window approach to find the minimum sum of a subarray. We keep a running sum of the elements in the window and update the minimum sum whenever we encounter a smaller sum. If the running sum exceeds 0, we reset it to 0 because a positive sum will only increase the minimum sum.