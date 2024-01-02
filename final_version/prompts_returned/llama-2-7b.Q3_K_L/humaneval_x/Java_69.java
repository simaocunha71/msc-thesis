import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than
    zero, and has a frequency greater than or equal to the value of the integer itself.
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search(Arrays.asList(4, 1, 2, 2, 3, 1)) == 2
        search(Arrays.asList(1, 2, 2, 3, 3, 3, 4, 4, 4)) == 3
        search(Arrays.asList(5, 5, 4, 4, 4)) == -1
     */
    public int search(List<Integer> lst) {
        
        if (lst.isEmpty()) return -1;
        
        Map map = new HashMap();
        for (int i : lst)
            map.put(i, 0);
        
        return max(map.keySet().stream().filter(x -> x > 0).findFirst().get());
    }
    
     private int max(Collection<Integer> nums) {
        if (nums == null || nums.isEmpty()) return -1;
        
        // Iterator iter = new ArrayList(nums).iterator();
        int maxi = 0, i = 0;
        while (i < nums.size()) {
            int curVal = nums.get(i++);
            if (curVal > maxi) {
                maxi = curVal;
                // System.out.println("max: " + curVal);
            }
        }
        
        return maxi;
    }
    
}
