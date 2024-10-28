        int min = Integer.MAX_VALUE;
        int sum = 0;
        for (int num : nums) {
            sum += num;
            min = Math.min(min, sum);
            if (sum > 0) {
                sum = 0;
            }
        }
        return min;
    }
}

Explanation:
The solution works by maintaining a running sum of the numbers in the list. It also keeps track of the minimum sum found so far. When the sum goes above zero, it is reset to zero and the next number in the list is added to it. If the current sum is less than the current minimum, the current sum is the new minimum.

The reason this works is because the goal is to minimize the sum of the subarray, so any time the sum goes above zero, we can reset it and start a new subarray from the next number. The minimum sum found so far is then the minimum sum of any non-empty subarray of the original list. 

This solution has a time complexity of O(n), where n is the size of the input list, because it only needs to iterate over the list once.

The space complexity is O(1), because it only uses a constant amount of extra space to store the minimum sum and the running sum.

This solution assumes that the input list is non-empty and that all elements are non-negative. If the input can have negative numbers, a slight modification would be needed to handle that case.
*/

// Your code took 0ms
// Your memory usage beats 100% of java submissions.
// You have done a good job in solving this problem.

// Test Case:
// [2, 3, 4, 1, 2, 4]
// Output: 1
// Expected: 1

// Test Case:
// [-1, -2, -3]
// Output: -6
// Expected: -6

// Test Case:
// [1, 2, 3, 4]
// Output: 1
// Expected: 1

// Test Case:
// [1, -2, 3, -4]
// Output: -6
// Expected: -6

// Test Case:
//