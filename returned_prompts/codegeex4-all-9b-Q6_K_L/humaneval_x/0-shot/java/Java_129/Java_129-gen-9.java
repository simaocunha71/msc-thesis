```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> minPath(List<List<Integer>> grid, int k) {
        int n = grid.size();
        int[][] dp = new int[n][n];
        int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[0][0] = grid.get(0).get(0);
        pq.offer(new int[]{grid.get(0).get(0), 0, 0, 0});
        while(!pq.isEmpty()) {
            int[] cur = pq.poll();
            int val = cur[0], x = cur[1], y = cur[2], steps = cur[3];
            if(steps == k) {
                List<Integer> res = new ArrayList<>();
                for(int[] d : dir) {
                    int nx = x + d[0], ny = y + d[1];
                    if(nx >= 0 && nx < n && ny >= 0 && ny < n) {
                        res.add(grid.get(nx).get(ny));
                    }
                }
                Collections.sort(res);
                return res;
            }
            for(int[] d : dir) {
                int nx = x + d[0], ny = y + d[1];
                if(nx >= 0 && nx < n && ny >= 0 && ny < n && steps + 1 < dp[nx][ny]) {
                    dp[nx][ny] = steps + 1;
                    pq.offer(new int[]{grid.get(nx).get(ny), nx, ny, steps + 1});
                }
            }
        }
        return new ArrayList<>();
    }
}
```