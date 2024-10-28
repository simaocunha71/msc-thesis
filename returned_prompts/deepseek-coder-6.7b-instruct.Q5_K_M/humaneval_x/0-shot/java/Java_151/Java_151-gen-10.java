        int sum = 0;

        for (Object o : lst) {
            if (o instanceof Integer && (int) o % 2 == 1 && (int) o > 0) {
                sum += Math.pow((int) o, 2);
            }
        }

        return sum;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.doubleTheDifference(Arrays.asList(1, 3, 2, 0))); // Expected 10
        System.out.println(solution.doubleTheDifference(Arrays.asList(-1, -2, 0))); // Expected 0
        System.out.println(solution.doubleTheDifference(Arrays.asList(9, -2))); // Expected 81
        System.out.println(solution.doubleTheDifference(Arrays.asList(0))); // Expected 0
        System.out.println(solution.doubleTheDifference(Arrays.asList())); // Expected 0

    }
}

//src/main/java/com/java/interview/questions/leetcode/easy/TwoSum.java
package com.java.interview.questions.leetcode.easy;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[] { numMap.get(complement), i };
            } else {
                numMap.put(nums[i], i);
            }
        }
        return new int[] {};
    }
}

//src/main/java/com/java/interview/questions/Main.java
package com.java.interview.