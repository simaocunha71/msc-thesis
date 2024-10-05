import java.util.*;

class Solution {
    public int maxFill(List<List<Integer>> grid, int capacity) {
        int numRows = grid.size();
        int numCols = grid.get(0).size();

        int[] wellLevels = new int[numRows];
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                if (grid.get(i).get(j) == 1) {
                    wellLevels[i]++;
                }
            }
        }

        int numBuckets = 0;
        for (int i = 0; i < numRows; i++) {
            if (wellLevels[i] > 0) {
                int numBucketsNeeded = (int) Math.ceil((double) wellLevels[i] / capacity);
                numBuckets += numBucketsNeeded;
            }
        }

        return numBuckets;
    }
}

Explanation:
1. First, we calculate the number of units of water in each well. We do this by iterating through each cell in the grid and incrementing the corresponding well level if the cell contains a 1.

2. Next, we calculate the number of buckets needed for each well. We do this by dividing the well level by the bucket capacity and rounding up to the nearest integer.

3. Finally, we sum up the number of buckets needed for all wells and return the result.