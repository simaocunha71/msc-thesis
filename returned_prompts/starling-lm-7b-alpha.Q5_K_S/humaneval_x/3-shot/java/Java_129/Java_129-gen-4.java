        int n = grid.size();
        if (n == 0) return Collections.emptyList();

        int[][] directions = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };
        int[][] visited = new int[n][n];

        int[][] next_nodes = new int[n * n][];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = -1;
                next_nodes[grid[i][j]] = new int[] { i, j };
            }
        }

        int[] next_node_index = new int[n * n];
        Arrays.fill(next_node_index, -1);

        int[] next_nodes_list = new int[n * n];
        int next_nodes_list_len = 0;

        int[] next_nodes_list_index = new int[n * n];
        Arrays.fill(next_nodes_list_index, -1);

        int[] next_nodes_list_len_index = new int[n * n];
        Arrays.fill(next_nodes_list_len_index, -1);

        int[] next_nodes_list_len_list = new int[n * n];
        Arrays.fill(next_nodes_list_len_list, -1);

        int current_node_index = 0;
        int next_node_list_len = 1;

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            if (next_node_list_len == 0) {
                return result;
            }

            int current_node = next_nodes[current_node_index][0];
            int current_node_y = next_nodes[current_node_index][1];
            result.add(current_node);
            current_node_index = next_node_index[current_node];
            next_node_