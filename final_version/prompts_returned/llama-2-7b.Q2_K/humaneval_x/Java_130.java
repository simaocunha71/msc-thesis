import java.util.*;
import java.lang.*;

class Solution {
    /**
    Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8
    You are given a non-negative integer number n, you have to a return a list of the
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
     */
    public List<Integer> tri(int n) {
        int[] dp = new int[n+1];
        if (dp==null){ throw new NullPointerException();}
        for (int i=0;i<=d.length-2;++i){
            if (i%2!=0 && dp[i] == 0) {//Odd, add up 2*d, tri(n-1), and tri(n)
                dp[i] = tri(n-1)+tri(n);
            }else if ((i%2==0)&&dp[i]!=0){//Even, 3/2 * d + tri(n)
                dp[i]=d+tri(n);
            }
        }
        return Arrays.asList(new Integer[]{});
    }
}
