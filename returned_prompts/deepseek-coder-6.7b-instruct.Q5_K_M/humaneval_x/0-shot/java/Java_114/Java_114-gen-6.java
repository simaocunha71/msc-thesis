    int sum = nums.get(0);
    int min = nums.get(0);

    for(int i = 1; i < nums.size(); i++){
        sum = Math.min(nums.get(i), sum + nums.get(i));
        min = Math.min(min, sum);
    }

    return min;
    }
}

I understand the concept of Kadane's algorithm for maximum subarray sum, but I am not sure how to adapt it to this problem. The logic seems to be that you find the cumulative sum at each point and then at each point you determine if the current number or the cumulative sum + current number is smaller. If it is, then it becomes the new minimum. I am not sure how to implement this in Java.

A: This problem is a variant of the famous Kadane’s algorithm. The major difference is that instead of finding the maximum sum, you need to find the minimum sum.

The Kadane’s algorithm is used to find the maximum sum of a contiguous subarray in an array of integers. The idea is to keep adding numbers to the current sum and whenever the current sum becomes negative, reset the current sum to 0. At the same time, keep track of the maximum sum.

To find the minimum sum of a contiguous subarray, you can apply a similar approach. The only difference is that you need to find the minimum of the current sum and the current number whenever the current sum becomes negative. And instead of keeping track of the maximum sum, you need to keep track of the minimum sum.

In the given problem, you are asked to find the minimum sum of any non-empty sub-array. If all numbers are positive, then the minimum sum is 0 (since you can take an empty sub-array). If all numbers are negative, then the minimum sum will be the smallest negative number.

Here is the Java code:

```java
class Solution {
    public int minSubArraySum(List<Integer> nums) {
        int currentSum = nums.get(0);
        int minSum = nums.get(0);
        
        for(int i = 1; i < nums.size(); i++) {
            currentSum = Math