  // let's calculate the max number of times we need to lower the bucket
  // the max number of times we need to lower the bucket is the max number of times 
  // the bucket can fill the entire grid, which is the max number of times the bucket can fill a row

  const rowMaxFills = grid.map(row => {
    // this is the number of times the bucket can fill the row
    // if the bucket is of capacity 1, then it can fill the row once
    // if the bucket is of capacity 2, then it can fill the row twice
    // if the bucket is of capacity 3, then it can fill the row thrice
    return row.reduce((total, current) => (current === 1 ? total + 1 : total), 0);
  });

  // we need to find the max number of times the bucket can fill the entire grid
  // we can do this by finding the max number of times the bucket can fill any row
  const maxFillCount = Math.max(...rowMaxFills);

  // if the max number of times the bucket can fill the entire grid is greater than the capacity
  // then we need to lower the bucket
  // if the max number of times the bucket can fill the entire grid is less than or equal to the capacity
  // then we don't need to lower the bucket
  return maxFillCount > capacity ? maxFillCount : 0;
}

const grid = [
  [0,0,1,0],
  [0,1,0,0],
  [1,1,1,1]
];

const bucketCapacity = 1;

console.log(maxFill(grid, bucketCapacity));