  let rows = grid.length;
  let cols = grid[0].length;
  let bucketCount = 0;
  
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === 1) {
        bucketCount++;
      }
    }
  }
  
  return Math.ceil(bucketCount / capacity);
};

console.log(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)); // 6
console.log(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)); // 5
console.log(maxFill([[0,0,0], [0,0,0]], 5)); // 0
```

## Solution Explanation:
The main idea is to count all the 1s in the grid, which represents the amount of water in each well. After that, we divide the total amount of water by the bucket capacity to get the total number of buckets needed to empty all the wells. Since we can't have a fraction of a bucket, we use the `Math.ceil` function to round up the result to the nearest integer, which represents the number of times we need to lower the buckets. 

This solution has a time complexity of O(n*m) where n and m are the dimensions of the grid, and a space complexity of O(1) since we only store a constant number of variables.

## Solution Complexity:
Time Complexity: O(n*m)
Space Complexity: O(1)
where n and m are the dimensions of the grid.

## Solution Test Cases:
Test Case 1:
Input: grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]], bucket_capacity = 1
Output: 6

Test Case 2:
Input: grid = [[0,0,1