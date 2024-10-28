        int n = grid.size();
        for(int i = 0; i < n; i++) {
            if(grid.get(i).size() < k) {
                continue A;
            }
        }

        int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        List<Integer> cur = new ArrayList<>();
        List<Integer> res = new ArrayList<>();
        cur.add(grid.get(0).get(0));
        res.add(grid.get(0).get(0));
        while(cur.size() < k) {
            List<Integer> next = new ArrayList<>();
            for(int i = 0; i < cur.size(); i++) {
                int num = cur.get(i);
                for(int[] d : dir) {
                    int x = d[0] + i;
                    int y = d[1] + i;
                    if(x >= 0 && x < n && y >= 0 && y < grid.get(x).size()) {
                        if(grid.get(x).get(y) < num) {
                            next.add(grid.get(x).get(y));
                        }
                    }
                }
            }
            cur = next;
            Collections.sort(cur);
        }
        return res;
    }
}










































































































































































