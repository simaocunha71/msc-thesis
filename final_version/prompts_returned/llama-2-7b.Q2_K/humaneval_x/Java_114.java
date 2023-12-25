import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum(Arrays.asList(2, 3, 4, 1, 2, 4)) == 1
    minSubArraySum(Arrays.asList(-1, -2, -3)) == -6
     */
    public int minSubArraySum(List<Integer> nums) {
        // Your Code Here
        if (nums == null || nums.isEmpty()) return -1;
        
        Map<List<Integer>, Integer> map = new HashMap<>(4);
        map.put(Arrays.asList(-1), -1);
        for (int i : nums) {
            List<Integer> currentSubArray = Arrays.asList(i);
            
            if (!map.containsKey(currentSubArray)) {
                map.put(currentSubArray, 0);
            } else {
                int currMapSum = map.get(currentSubArray) + i;
                
                map.replaceEntry(currMapSum >= map.get(currentSubArray) ? currentSubArray : null,
                        map.get(currentSubArray) + 1);
            }
            
            if (map.get(currentSubArray) == Integer.MAX_VALUE) {
                return -1;
            }
        }
        
        return map.get(Collections.min(map.keySet())).intValue();
    }
}