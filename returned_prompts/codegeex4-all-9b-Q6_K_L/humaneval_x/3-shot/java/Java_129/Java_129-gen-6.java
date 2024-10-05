        int N = grid.size();
        int[][] distance = new int[N][N];
        int[][] parent = new int[N][N];
        int[][] direction = {{0,1},{0,-1},{1,0},{-1,0}};
        boolean[][] visited = new boolean[N][N];
        Queue<int[]> queue = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        queue.add(new int[]{0, 0, 0, 0});
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            visited[current[0]][current[1]] = true;
            distance[current[0]][current[1]] = current[2];
            if (current[2] == k) {
                return getParent(current[0], current[1], N, parent, grid);
            }
            for (int[] dir : direction) {
                int x = current[0] + dir[0], y = current[1] + dir[1];
                if (x >= 0 && x < N && y >= 0 && y < N && !visited[x][y]) {
                    queue.add(new int[]{x, y, current[2] + 1, current[3]});
                    parent[x][y] = current[3];
                }
            }
        }
        return new ArrayList<>();
    }

    private List<Integer> getParent(int x, int y, int N, int[][] parent, List<List<Integer>> grid) {
        List<Integer> result = new ArrayList<>();
        result.add(grid.get(x).get(y));
        int parent_x = x, parent_y = y;
        while (parent_x != 0 || parent_y != 0) {
            result.add(grid.get(parent_x).get(parent_y));
            int temp = parent_x;
            parent_x = parent_y;
            parent_y = temp;
        }
        Collections.reverse(result);
        return result;
    }
}

