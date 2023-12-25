import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> orderByPoints(Arrays.asList(1, 11, -1, -11, -12)) == [-1, -11, 1, -12, 11]
    >>> orderByPoints(Arrays.asList()) == []
     */
    public List<Integer> orderByPoints(List<Integer> nums) {
        // sort the list in ascending order according to sum of their digits
        Collections.sort(nums);
        
        // get the index (position) of each digit in its sorted list
        Set<Integer> indices = new HashSet<>();
        for (int i=0;i<nums.size();++i){
            Integer j = nums.get(i); 
            if (indices.add(j)) {
                // add the index of digit in its sorted position
                j = indices.size()-1;
                System.out.printf("%d ", j);
            } else {
                System.err.println("duplicate index of a digit, use -1 to indicate this!");
            }
        } 
        
        // sort the list again in order of their indices
        Collections.sort(nums, (a,b)->{  
          int i = Integer.compare(indices.get(a), indices.get(b));
          return(i == 0) ? a : i;  
        }); 
        
        return nums;
    }
}
