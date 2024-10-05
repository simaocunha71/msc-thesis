        // BFS solution
        int n = grid.size();
        int m = grid.get(0).size();
        int[][] dist = new int[n][m];
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        PriorityQueue<Node> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }
        dist[0][0] = 0;
        pq.offer(new Node(0, 0, 0, null));
        List<Integer> ans = new ArrayList<>();
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (cur.val == k) {
                break;
            }
            for (int[] dir : dirs) {
                int x = cur.i + dir[0];
                int y = cur.j + dir[1];
                if (x < 0 || y < 0 || x == n || y == m || dist[x][y] <= cur.dist) {
                    continue;
                }
                dist[x][y] = cur.dist + 1;
                pq.offer(new Node(x, y, dist[x][y], cur.path));
                if (cur.path == null) {
                    cur.path = new ArrayList<>();
                }
                cur.path.add(grid.get(cur.i).get(cur.j));
            }
        }
        for (int[] row : dist) {
            for (int cell : row) {
                if (cell == Integer.MAX_VALUE) {
                    continue;
                }
                ans.add(cell);
            }
        }
        return ans;
    }
}

class Node {
    int i;
    int j;
    int dist;
    List<Integer> path;

    public Node(int i, int j, int dist, List