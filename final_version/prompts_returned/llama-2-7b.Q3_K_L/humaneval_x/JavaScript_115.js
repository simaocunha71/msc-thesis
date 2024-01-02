/*
  You are given a rectangular grid of wells. Each row represents a single well,
  and each 1 in a row represents a single unit of water.
  Each well has a corresponding bucket that can be used to extract water from it, 
  and all buckets have the same capacity.
  Your task is to use the buckets to empty the wells.
  Output the number of times you need to lower the buckets.

  Example 1:
      Input: 
          grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
          bucket_capacity : 1
      Output: 6

  Example 2:
      Input: 
          grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
          bucket_capacity : 2
      Output: 5
  
  Example 3:
      Input: 
          grid : [[0,0,0], [0,0,0]]
          bucket_capacity : 5
      Output: 0

  Constraints:
      * all wells have the same length
      * 1 <= grid.length <= 10^2
      * 1 <= grid[:,1].length <= 10^2
      * grid[i][j] -> 0 | 1
      * 1 <= capacity <= 10
  */
const maxFill = (grid, capacity) => {
    let minIndex = 0;
    for(let row of grid) {
        if(row.length !== 0){
            break;
        } else {
            minIndex++;
        }
    }
    
    let fillCount = 1;
    let maxBucket = capacity - minIndex + 1; // if we have a bucket with the same capacity as grid[row,col], use it to extract all the water from that row before going further.
    for(let i=minIndex+1;i<grid.length+maxBucket-2;i++){
        let rowCount = 0;
        
        for(let