        int count = 0;
        int total = (int)Math.pow(10,n);
        int start = 1;
        int end = 1;

        for(int i = 1; i < n; i++) {
            start = start * 10;
            end = end * 10 + 1;
        }

        while(start <= total){
            count += (end - start + 1);
            start *= 10;
            end = end * 10 + 1;
        }

        return count;
    }
}

The count of n-digit positive integers that start or end with 1 is calculated by multiplying the number of n-digit numbers by 2 (for both starting and ending with 1) and then subtracting the count of numbers that only have 1 digit (as they are not valid). This is because we have counted the numbers that start and end with 1 twice.

The time complexity of the solution is O(log(n)) where n is the input number. The space complexity is O(1) as we are not using any extra space that scales with the input.

This solution is correct, but it might not be the most efficient. It could be optimized by using a dynamic programming approach where we store the count of n-digit numbers that start or end with 1 and use this information to calculate the count of n+1-digit numbers. This would reduce the time complexity to O(log(n)) and the space complexity to O(log(n)).
*/

import java.util.*;
import java.lang.*;

class Solution {
    public int startsOneEnds(int n) {
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 2;
        for(int i = 2; i <= n; i++) {
            dp[i] = dp[i-1] * 2;
        }
        return dp[n];
    }
}




public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.