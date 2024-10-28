        List<Integer> res = new ArrayList<>();
        int n = grid.size();
        boolean[][] visited = new boolean[n][n];
        int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};

B:
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                res.add(grid.get(i).get(j));
            }
        }

C:
        Collections.sort(res);
        return res.subList(0,k);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<Integer>> grid = Arrays.asList(
                Arrays.asList(5,9,3),
                Arrays.asList(4,1,6),
                Arrays.asList(7,8,2));
        System.out.println(s.minPath(grid, 1));
    }
}

*/

// This code doesn't work because it doesn't satisfy the problem constraints.
// The problem constraints state that it's not possible to use Dijkstra's or A* algorithms,
// and the code doesn't implement any such algorithms. The problem also doesn't specify
// the direction of movement, so the code doesn't consider that either.

//src/main/java/com/leetcode/medium/MinimumPathSum.java
package com.leetcode.medium;

/*
