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
        int sum = 0;
        
       for (int i=0;i < nums.size();i++){  
            if(nums.get(i)+sum >= 0){   
               sum += nums.get(i);   
            }else{  
               sum -= nums.get(i);  
            }                            
       }     
       
        return sum;
    }
}