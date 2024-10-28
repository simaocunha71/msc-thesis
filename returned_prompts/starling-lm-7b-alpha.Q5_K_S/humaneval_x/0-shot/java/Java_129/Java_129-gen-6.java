        if(k == 0) {
            return new ArrayList<>();
        }

        int[][] dir = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        List<List<Integer>> candidates = new ArrayList<>();
        for(int i = 0; i < grid.size(); ++i) {
            for(int j = 0; j < grid.get(i).size(); ++j) {
                candidates.add(new ArrayList<>(Arrays.asList(i, j, grid.get(i).get(j))));
            }
        }
        Collections.sort(candidates, (candidateA, candidateB) -> {
            return Integer.compare(candidateA.get(2), candidateB.get(2));
        });
        int[][] visited = new int[grid.size()][grid.size()];
        List<Integer> result = new ArrayList<>();
        while(k > 0) {
            int[] coord = candidates.get(0);
            if(visited[coord[0]][coord[1]] != 0) {
                candidates.remove(0);
                continue A;
            }
            visited[coord[0]][coord[1]] = visited[coord[0]][coord[1]] == 0 ? 1 : visited[coord[0]][coord[1]] + 1;
            result.add(coord[2]);
            k--;
            for(int[] dirA : dir) {
                int[] next = new int[]{coord[0]+dirA[0], coord[1]+dirA[1]};
                if(!isValid(grid, next)) {
                    continue;
                }
                int index = findIndex(candidates, next);
                if(index == -1) {
                    continue;
                }
                candidates.remove(index);
            }
        }
        Collections.reverse(result);
        return result;
    }

    private boolean isValid(List<List<Integer>> grid, int[] coord) {
        return coord[0] >= 0 && coord[0] < grid.size() && coord[1