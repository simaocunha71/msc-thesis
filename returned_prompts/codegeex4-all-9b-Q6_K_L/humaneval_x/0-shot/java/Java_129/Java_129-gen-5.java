```java
import java.util.*;

class Solution {
    private static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private static final int[][] DIRECTIONS2 = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private int n;
    private int[][] grid;
    private int[][][] dp;
    private int[][][] dist;
    private int[][][] parent;
    private int[][][] parent2;

    public List<Integer> minPath(List<List<Integer>> grid, int k) {
        this.n = grid.size();
        this.grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                this.grid[i][j] = grid.get(i).get(j);
            }
        }
        this.dp = new int[n][n][k + 1];
        this.dist = new int[n][n][n];
        this.parent = new int[n][n][k + 1];
        this.parent2 = new int[n][n][k + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(dp[i][j], Integer.MAX_VALUE);
                Arrays.fill(dist[i][j], Integer.MAX_VALUE);
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dijkstra(i, j);
            }
        }
        int x = 0, y = 0, step = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j][k] < dp[x][y][k]) {
                    x = i;
                    y = j;
                }
            }
        }
        List<Integer> res = new ArrayList<>();
        while (step >= 0) {
            res.add(grid[x][y]);
            int nx = parent[x][y][step];
            int ny = parent2[x][y][step];
            if (nx == x && ny == y) {
               