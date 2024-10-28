        List<Integer> result = new ArrayList<Integer>();
        int n = grid.size();
        int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->{
            for(int i=0;i<a.length;i++){
                if(a[i]==b[i]) continue;
                return Integer.compare(a[i],b[i]);
            }
            return 0;
        });

        pq.add(new int[]{grid.get(0).get(0), 0, 0, 0});
        boolean[][][] visited = new boolean[n][n][k+1];
        visited[0][0][0] = true;

        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            if(cur[2]==k){
                result = new ArrayList<>();
                for(int i=0;i<cur.length-1;i++){
                    result.add(cur[i]);
                }
                return result;
            }
            for(int[] dir: directions){
                int x = cur[1]+dir[0], y = cur[2]+dir[1], steps = cur[3]+1;
                if(x<0||x>=n||y<0||y>=n||visited[x][y][steps]||steps>k) continue;
                visited[x][y][steps] = true;
                pq.add(new int[]{grid.get(x).get(y), x, y, steps});
            }
        }
        return result;
    }
}

This solution uses Dijkstra's shortest path algorithm with a priority queue. It keeps track of the cell value, x-coordinate, y-coordinate, and the step number. 

It starts from the top left cell, and for each cell, it adds all its neighbors to the priority queue. It continues this until it reaches the cell with k steps. The priority queue is ordered by the cell values, so it always chooses the smallest