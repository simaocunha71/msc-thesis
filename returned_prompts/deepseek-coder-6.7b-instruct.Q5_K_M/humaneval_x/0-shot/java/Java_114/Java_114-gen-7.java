        int sum = nums.get(0);
        int min = nums.get(0);

        for(int i=1; i<nums.size(); i++){
            sum = Math.min(nums.get(i), sum + nums.get(i));
            min = Math.min(min, sum);
        }

        return min;
    }
}

This program uses Kadane's algorithm to find the minimum sum of any non-empty subarray. It iteratively checks the current number and the sum of the current number and the previous sum. The sum is updated if the current number is smaller. The minimum sum is updated if the current sum is smaller.

It starts with the first number as the sum and minimum, then iterates through the rest of the array. In each iteration, it checks if the current number is smaller than the current sum plus the current number, and if it is, it updates the sum. It then checks if the current sum is smaller than the minimum, and if it is, it updates the minimum.

After going through the entire array, the minimum sum is returned.

This program runs in O(n) time, where n is the size of the input array, because it only needs to go through the array once. It also runs in O(1) space, because it only uses a constant amount of space to store the sum and minimum.

This program handles negative numbers correctly because it treats negative numbers as potential subarray sums and compares them to zero. If a negative number is smaller than zero, it will be treated as a potential minimum subarray sum.

This program also handles the case where the array is empty by returning 0, because if the array is empty, the minimum sum is undefined.
*/

// 