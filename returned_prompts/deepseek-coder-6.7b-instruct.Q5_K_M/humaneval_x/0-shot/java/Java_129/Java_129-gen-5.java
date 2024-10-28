        int N = grid.size();
        int[][] directions = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
        List<Integer> result = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] == b[2] ? a[0] * a[1] - b[0] * b[1] : a[2] - b[2]);
        boolean[][] visited = new boolean[N][N];
        pq.offer(new int[]{0, 0, grid.get(0).get(0