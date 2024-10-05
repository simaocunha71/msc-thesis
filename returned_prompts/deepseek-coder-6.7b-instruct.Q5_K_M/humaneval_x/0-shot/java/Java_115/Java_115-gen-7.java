        int steps = 0;
        int[] buckets = new int[grid[0].size()];
        int[][] gridArr = new int[grid.size()][grid[0].size()];

        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[0].size(); j++) {
                gridArr[i][j] = grid.get(i).get(j);
            }
        }

        for(int j = 0; j < grid[0].size(); j++) {
            for(int i = 0; i < grid.size(); i++) {
                if(gridArr[i][j] == 1) {
                    buckets[j]++;
                }
            }
        }

        while(!Arrays.equals(buckets, new int[buckets.length])) {
            Arrays.sort(buckets);
            if(buckets[0] < capacity) {
                buckets[0]++;
                steps++;
            }
        }
        return steps;
    }
}

Here's what I've done:
- I first convert the 2D List to a 2D array to make it easier to work with.
- I then create an array of buckets to hold the amount of water in each well.
- I iterate over the grid, increasing the water level in each bucket corresponding to a well.
- Lastly, I use a while loop to continually lower the water level in the bucket with the least water until all the buckets are full.
- I count the number of times the buckets are lowered.

This solution works, but it's not optimal. The time complexity is O(n^2) due to the nested for loop, and the space complexity is O(n) for the bucket array.

I need to find an optimal solution with better time and space complexity.

I'd appreciate any suggestions on how to improve this code.
*/

//P:
// An optimal solution would be to use a priority queue to keep track of the empty spaces in the grid.
// The priority queue will be sorted by the number of water units in each well