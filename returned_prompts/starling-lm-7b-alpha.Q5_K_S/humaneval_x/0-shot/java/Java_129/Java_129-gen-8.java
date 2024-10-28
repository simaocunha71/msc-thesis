        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        List<List<Integer>> path = new ArrayList<>();
        path.add(grid.get(0));
        path.add(grid.get(1));

        List<Integer> res = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();

        while (res.size() < k) {
            visited.clear();
            int prev = res.size();
            for (int i = 0; i < path.size(); i++) {
                for (int j = 0; j < path.get(i).size(); j++) {
                    int val = path.get(i).get(j);
                    if (visited.contains(val)) {
                        continue;
                    }
                    if (res.size() == k) {
                        break A;
                    }
                    visited.add(val);
                    res.add(val);
                }
            }

            for (int i = 0; i < path.size(); i++) {
                for (int j = 0; j < path.get(i).size(); j++) {
                    int val = path.get(i).get(j);
                    if (visited.contains(val)) {
                        continue;
                    }
                    for (int[] d : directions) {
                        int r = i + d[0];
                        int c = j + d[1];
                        if (r < 0 || r >= path.size() || c < 0 || c >= path.get(r).size()) {
                            continue;
                        }
                        int nval = path.get(r).get(c);
                        if (visited.contains(nval)) {
                            continue;
                        }
                        path.add(new ArrayList<>(path.get(r)));
                        path.get(path.size() - 1).add(nval);
                        break;
                    }
                }
            }
        }
        return res;
   