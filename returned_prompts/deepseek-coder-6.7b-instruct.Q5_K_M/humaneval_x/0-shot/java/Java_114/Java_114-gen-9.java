        int min = Integer.MAX_VALUE;
        int currentSum = 0;

        for (int num : nums) {
            currentSum = Math.min(currentSum + num, num);
            min = Math.min(min, currentSum);
        }

        return min;
    }
}

Explanation:
This problem is a variation of the "Minimum Subarray Sum" problem which is a well-known problem in dynamic programming.

We maintain a "currentSum" variable which represents the sum of the current subarray. At each element in nums, we update currentSum to be the minimum of the current element and the sum of the current element and the previous currentSum.

The reason we do this is that we want to start a new subarray if the current element is smaller than the previous subarray sum, because a smaller element will yield a smaller sum.

We also keep track of the minimum sum we've seen so far in the "min" variable. At each step, we update min to be the minimum of the current sum and the previous min.

Finally, we return the minimum sum we've seen.

The time complexity of this solution is O(n), where n is the size of nums, because we only iterate over nums once. The space complexity is O(1), because we only use a constant amount of space to store our current sum and minimum.

This solution works because it finds the smallest subarray sum by always considering the smallest possible sum at each step.

Note: This solution assumes that the input list is not empty. If the input list could be empty, you should add a check for this in your code.

*/

// 1. The time complexity of this solution is O(n), where n is the size of nums, because we only iterate over nums once.
// 2. The space complexity is O(1), because we only use a constant amount of space to store our current sum and minimum.
// 3. This solution works because it finds the smallest subarray sum by always considering the smallest possible sum at each step.
// 4. Note: This solution assumes that the input list is not empty. If the input list could be empty, you should add a check for this in your code.








