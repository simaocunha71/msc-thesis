    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid.length; j++) {
            if (grid[i][j] <= k) {
                if (i > 0 && j > 0) {
                    grid[i][j] = Math.min(grid[i][j], grid[i - 1][j - 1]);
                }
                if (i > 0 && j < grid.length - 1) {
                    grid[i][j] = Math.min(grid[i][j], grid[i - 1][j + 1]);
                }
                if (i < grid.length - 1 && j > 0) {
                    grid[i][j] = Math.min(grid[i][j], grid[i + 1][j - 1]);
                }
                if (i < grid.length - 1 && j < grid.length - 1) {
                    grid[i][j] = Math.min(grid[i][j], grid[i + 1][j + 1]);
                }
                continue A;
            }
        }
    }
    return grid[k % grid.length][k / grid.length];
};

/*
Explanation:
We can use the Dijkstra’s algorithm to solve this problem.
We can transform this problem into a graph problem. In the graph, each node is a value on the grid.
The weight of each edge is the Manhattan distance between the two corresponding nodes.
Then, we can use Dijkstra’s algorithm to find the shortest path from the starting node to all the other nodes.
The time complexity of Dijkstra’s algorithm is O(ElogE), where E is the number of edges.
The space complexity is O(V+E), where V is the number of vertices.

We can optimize the space complexity to O(V) by using a priority queue, and we can optimize the time complexity to O(E)
by using the following optimization:

For each node, we only need to consider its 4 neighbors.
For each neighbor, if its Manhattan distance is