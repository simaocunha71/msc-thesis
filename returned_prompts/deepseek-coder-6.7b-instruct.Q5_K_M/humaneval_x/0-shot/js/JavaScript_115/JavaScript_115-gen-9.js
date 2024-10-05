  let count = 0;
  for(let i = 0; i < grid.length; i++){
      for(let j = 0; j < grid[i].length; j++){
          if(grid[i][j] === 1){
              count++;
          }
      }
  }
  return Math.ceil(count / capacity);
}

console.log(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)); //6
console.log(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)); //5
console.log(maxFill([[0,0,0], [0,0,0]], 5)); //0



A: The problem is to find the minimum number of times a bucket should be filled to empty all the wells. The bucket capacity is given, which is 1 in all the examples. So, we can just count the number of 1's in the grid, which represents the number of wells that have water in them. And then we divide that count by the bucket's capacity to get the number of times we need to fill the bucket.

We use the Math.ceil() function to round up the result to the nearest whole number, because we can't have a fraction of a bucket.

In the end, we return the count.
*/


A: The problem is to find the minimum number of times a bucket should be filled to empty all the wells. The bucket capacity is given, which is 1 in all the examples. So, we can just count the number of 1's in the grid, which represents the number of wells that have water in them. And then we divide that count by the bucket's capacity to get the number of times we need to fill the bucket.

We use the Math.ceil() function to round up the result to the nearest whole number, because we can't have a fraction of a bucket.

In the end, we return the count.
*/


A: The problem is to find the minimum number of times a bucket should be filled to