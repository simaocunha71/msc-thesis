import java.util.*;
import java.lang.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Initialize two variables to keep track of the indices of the two elements to return.
        int firstIndex = 0;
        int secondIndex = nums.length - 1;

        // Loop through the array of numbers.
        for (int i = 0; i < nums.length; i++) {
            // If the current number is equal to the target minus the current number, 
            // find the other number by subtracting it from the target.
            if (nums[i] == target - nums[i]) {
                // If the current number is less than the target, 
                // the other number must be greater than the current number.
                if (nums[i] < target) {
                    secondIndex = i;
                // If the current number is greater than the target, 
                    // the other number must be less than the current number.
                    } else {
                        firstIndex = i;
                    }
            }
        }

        // Return an array containing the indices of the two elements to return.
        return new int[] {firstIndex, secondIndex};
    }
}
