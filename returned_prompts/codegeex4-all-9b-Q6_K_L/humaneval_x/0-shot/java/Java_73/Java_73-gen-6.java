import java.util.*;
import java.lang.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        if (arr == null || arr.size() == 0) {
            return 0;
        }

        int n = arr.size();
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    dp[i][j] = 0;
                } else if (arr.get(i) == arr.get(j)) {
                    dp[i][j] = dp[i + 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i + 1][j], dp[i][j - 1]) + 1;
                }
            }
        }

        return dp[0][n - 1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.smallestChange(Arrays.asList(1, 2, 3, 5, 4, 7, 9, 6))); // 4
        System.out.println(sol.smallestChange(Arrays.asList(1, 2, 3, 4, 3, 2, 2))); // 1
        System.out.println(sol.smallestChange(Arrays.asList(1, 2, 3, 2, 1))); // 0
    }
}