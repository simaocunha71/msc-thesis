        int sum = 0;
        int min = Integer.MAX_VALUE;
        for(int num : nums) {
            sum += num;
            if(sum < min) {
                min = sum;
            }
            sum = Math.min(sum, num);
        }
        return min;
    }
}

The logic in the above code is to find the minimum sum of subarrays. 

The variable "sum" is used to keep track of the sum of the numbers in the current subarray. The variable "min" is used to keep track of the minimum sum found so far. 

For each number in the input list, we add it to the sum and then check if the sum is less than the current minimum. If it is, we update the minimum. We also update the sum to be the minimum of the current sum and the number. This ensures that the sum never decreases, which is a characteristic of the minimum sum of subarrays.

In the end, we return the minimum sum found.

This solution has a time complexity of O(n) and a space complexity of O(1), where n is the size of the input list.

It's worth noting that this solution assumes that the input list is not empty. If the input list can be empty, you should add a check for this condition at the start of the method.

Also, this solution assumes that the input list contains only non-negative integers. If the input list can contain negative integers, you should add a check for this condition and update the logic accordingly.

The solution is a Java implementation of the Kadane's algorithm, which is a popular algorithm for this problem.
*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minSubArraySum(Arrays.asList(2, 3, 4, 1, 2, 4)));  // Expected output: 1
        System.out.println(sol.minSubArraySum(Arrays.asList(-1, -2, -3)));  // Expected output: -6
    }
}
```

This solution is a java implementation of Kadane's algorithm. The time complexity of this solution