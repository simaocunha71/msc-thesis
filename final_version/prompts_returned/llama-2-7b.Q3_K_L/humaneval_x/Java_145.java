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
        // your code here
        List<Integer> result = new LinkedList<>();
	Collections.sort(nums);
        for (int n : nums) {
        	int sum = 0;
    		for (int i = 1; i < n; i++) {
           		sum += i;
                }
            
          if (sum > 9) {
              int[] arrayOfInt = Integer.toString(n).chars().mapToObj(c -> c-48).toArray();
              result.add(arrayOfInt[0]+arrayOfInt[1]);
            } else {
              result.add((int) n);
            }   
        }
    	return result;
    }
}