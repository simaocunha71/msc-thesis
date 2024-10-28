import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> minPath(List<List<Integer>> grid, int k) {
        int n = grid.size();
        int[][] dp = new int[n][n];
        int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int[][] dist = new int[n][n];
        Queue<int[]> q = new LinkedList<>();
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
                dist[i][j] = Integer.MAX_VALUE;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                q.offer(new int[]{i, j});
                dp[i][j] = grid.get(i).get(j);
                dist[i][j] = 0;
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];

            if (dist[x][y] == k) {
                continue;
            }

            for (int[] d : dir) {
                int nx = x + d[0];
                int ny = y + d[1];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }

                if (dist[nx][ny] > dist[x][y] + 1) {
                    dist[nx][ny] = dist[x][y] + 1;
                    q.offer(new int[]{nx, ny});
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] <= k) {
                    min = Math.min(min, dp[i][j]);
                }
            }
        }

        List<Integer> res = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] == min) {
                    res.add(grid.get(i).get