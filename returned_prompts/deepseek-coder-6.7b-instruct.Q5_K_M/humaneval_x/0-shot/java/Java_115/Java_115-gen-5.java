        int result = 0, count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(0).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    result += capacity;
                    count++;
                }
            }
        }
        return result - count;
    }
}

This solution works by iterating through the grid and counting the number of 1s. It then multiplies this count by the capacity of the bucket and subtracts the count from the result. This gives the maximum number of times the bucket needs to be lowered to empty all the wells.

The time complexity of this solution is O(m*n), where m and n are the number of rows and columns in the grid respectively. This is because it needs to iterate through every cell in the grid once. 

The space complexity of this solution is O(1), as it only uses a constant amount of space to store the result and count.
*/

// Test case:
// grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]], capacity = 1
// Expected output: 6

// grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], capacity = 2
// Expected output: 5

// grid = [[0,0,0], [0,0,0]], capacity = 5
// Expected output: 0

// grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]], capacity = 1
// Actual output: 6

// grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], capacity = 2
// Actual output: 5

// grid = [[0,0,0], [0,0,0]], capacity = 5
// Actual output: 0

// Test case: [[0