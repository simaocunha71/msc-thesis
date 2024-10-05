import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> minPath(List<List<Integer>> grid, int k) {
        int n = grid.size();
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = -1;
            }
        }
        int min = Integer.MAX_VALUE;
        int[] pos = new int[2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int dist = dfs(grid, i, j, 0, k, dp);
                if (dist < min) {
                    min = dist;
                    pos[0] = i;
                    pos[1] = j;
                }
            }
        }
        List<Integer> res = new ArrayList<>();
        dfsPath(grid, pos[0], pos[1], 0, k, dp, res);
        return res;
    }

    private int dfs(List<List<Integer>> grid, int i, int j, int dist, int k, int[][] dp) {
        if (dist == k) {
            return grid.get(i).get(j);
        }
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        int n = grid.size();
        int min = Integer.MAX_VALUE;
        if (i > 0) {
            min = Math.min(min, dfs(grid, i - 1, j, dist + 1, k, dp));
        }
        if (i < n - 1) {
            min = Math.min(min, dfs(grid, i + 1, j, dist + 1, k, dp));
        }
        if (j > 0) {
            min = Math.min(min, dfs(grid, i, j - 1, dist + 1, k, dp));
        }
        if (j < n - 1) {
            min = Math.min(min, dfs(grid, i, j + 1, dist + 1, k, dp));
        }
        dp[i][j] = min;
        return min;
    }

    private void dfsPath(List<List<Integer>> grid, int i, int j, int dist, int k, int[][] dp, List<Integer>