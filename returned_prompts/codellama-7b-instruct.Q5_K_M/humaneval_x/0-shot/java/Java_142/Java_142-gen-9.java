import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        // your code goes here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i=0;i<n;i++)
        {
            a[i] = sc.nextInt();
        }
        int[] dp = new int[n+1];
        
        dp[0] = 0;
        for(int i=1;i<=n;i++)
        {
            if(a[i-1] > 0)
                dp[i] = dp[i-1] + a[i-1];
            else
                dp[i] = dp[i-1];
        }
        int max = 0;
        for(int i=1;i<=n;i++)
        {
            if(dp[i] > max)
                max = dp[i];
        }
        System.out.println(max);
    }
}

