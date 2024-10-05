        int N = grid.size();
        List<Integer> result = new ArrayList<>();
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Queue<Integer> queue = new LinkedList<>();
                Set<String> visited = new HashSet<>();
                boolean found = false;

                queue.add(grid.get(i).get(j));
                visited.add(String.valueOf(i) + "," + String.valueOf(j));

                while (!queue.isEmpty() && !found) {
                    int current = queue.poll();

                    for (int[] direction : directions) {
                        int ni = i + direction[0];
                        int nj = j + direction[1];

                        if (ni >= 0 && ni < N && nj >= 0 && nj < N && !visited.contains(String.valueOf(ni) + "," + String.valueOf(nj))) {
                            queue.add(grid.get(ni).get(nj));
                            visited.add(String.valueOf(ni) + "," + String.valueOf(nj));

                            if (queue.size() == k) {
                                found = true;
                                break;
                            }
                        }
                    }

                    if (found) break;
                }

                if (found) {
                    result.add(current);
                }
            }
        }

        return result;
    }
}

