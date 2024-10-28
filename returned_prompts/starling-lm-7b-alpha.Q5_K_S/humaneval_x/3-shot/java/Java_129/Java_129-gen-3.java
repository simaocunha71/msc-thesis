        int N = grid.size();
        int[][] grid_array = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                grid_array[i][j] = grid.get(i).get(j);
            }
        }

        // First, we need to find all the numbers that appear in the grid,
        // and sort them.
        Set<Integer> all_numbers = new HashSet<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                all_numbers.add(grid_array[i][j]);
            }
        }
        List<Integer> all_numbers_list = new ArrayList<>(all_numbers);
        Collections.sort(all_numbers_list);

        // Now, we will map all the numbers that appear in grid to their index
        // in the list of all numbers.
        Map<Integer, Integer> index_map = new HashMap<>();
        for (int i = 0; i < all_numbers_list.size(); i++) {
            index_map.put(all_numbers_list.get(i), i);
        }

        // For each number, we will find the minimum path that uses this number
        // as the starting number.
        List<List<Integer>> path_list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                path_list.add(minPath(grid_array, index_map.get(grid_array[i][j]), k));
            }
        }

        // Now, we need to find the minimum path out of all the paths.
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int min_index = 0;
            for (int j = 0; j < path_list.size(); j++) {
                if (path_list.get