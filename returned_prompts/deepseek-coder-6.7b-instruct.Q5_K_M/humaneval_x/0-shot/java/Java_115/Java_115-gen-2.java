        int count = 0;
        int rows = grid.size();
        int cols = grid.get(0).size();
        int totalBuckets = 0;

        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                if(grid.get(i).get(j) == 1) {
                    totalBuckets++;
                }
            }
        }

        count = totalBuckets/capacity;
        if(totalBuckets % capacity != 0) count++;

        return count;
    }
}

This solution works by first determining the total number of wells represented by 1's in the grid. Then, it divides this total by the bucket capacity to determine the total number of times the bucket needs to be lowered, rounding up if necessary. The function then returns this count.

Test case 1:
Input: 
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]], capacity = 1
Output: 
    6

Test case 2:
Input: 
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], capacity = 2
Output: 
    5

Test case 3:
Input: 
    grid = [[0,0,0], [0,0,0]], capacity = 5
Output: 
    0

In all three test cases, the solution correctly calculates the number of times the bucket needs to be lowered to empty all the wells.
*/

//Test cases:
//[[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2
//[[0,0,0], [0,0,0]], 5
//[[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1
//All should return the correct count of buckets needed to be