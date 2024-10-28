        int n = grid.size();
        List<Integer> result = new ArrayList<>();
        int[][] dist = new int[n][n];

        // initialize distance matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = grid.get(i).get(j);
            }
        }

        // find the minimum distance of each cell
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int d = 1; d <= k; d++) {
                    int[][] new_dist = new int[n][n];
                    for (int a = 0; a < n; a++) {
                        for (int b = 0; b < n; b++) {
                            new_dist[a][b] = dist[a][b];
                        }
                    }
                    for (int a = 0; a < n; a++) {
                        for (int b = 0; b < n; b++) {
                            if (new_dist[a][b] != Integer.MAX_VALUE) {
                                for (int c = 0; c < n; c++) {
                                    if (c != a && c != b && new_dist[c][a] != Integer.MAX_VALUE && new_dist[c][b] != Integer.MAX_VALUE) {
                                        new_dist[a][b] = Math.min(new_dist[a][b], new_dist[c][a] + new_dist[c][b]);
                                    }
                                }
                            }
                        }
                    }
                    dist = new_dist;
                }
            }
        }

        // find the minimum path
        for (int i = 