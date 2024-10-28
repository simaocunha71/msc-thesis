import java.util.*;
import java.lang.*;

class Solution {
    /**
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circularShift(12, 1)
    "21"
    >>> circularShift(12, 2)
    "12"
     */
    public String circularShift(int x, int shift) {
        String s = String.valueOf(x);
        int len = s.length();
        int pos = shift%len;
        if(pos == 0) return s;
        return s.substring(len-pos)+s.substring(0,len-pos);
    }

    /**
    Given a list of integers, return a list where each index is the product of all the integers except the one at that index.
    For example, [1,2,3,4] should return [12,24,36,48]
    >>> productExceptSelf([1,2,3,4])
    [12,24,36,48]
     */
    public List<Integer> productExceptSelf(List<Integer> nums) {
        List<Integer> res = new ArrayList<Integer>();
        int n = nums.size();
        int[] dp = new int[n];
        dp[0] = 1;
        for(int i=1; i<n; i++){
            dp[i] = dp[i-1]*nums.get(i-1);
        }
        for(int i=n-2; i>=0; i--){
            dp[i] *= nums.get(i+1);
        }
        for(int i=0; i<n; i++){
            res.add(dp[i]);
        }
        return res;
    }
}
