import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
     */
    public int addElements(List<Integer> arr, int k) {
        // Your code here
        int sum = 0;
        Collections.sort(arr);// O(nlogn)
        
        for (int i = 1; i < Math.min(k, arr.size()); ++i){
            if (i > 2 && !(arr[i-3] < arr[i])){
                continue;
            }
            
            sum += arr[i];
        }
        
        return sum;
    }
}