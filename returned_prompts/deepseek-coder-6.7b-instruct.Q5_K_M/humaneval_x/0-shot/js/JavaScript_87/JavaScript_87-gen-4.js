  let result = [];
  
  for(let i = 0; i < lst.length; i++){
    for(let j = 0; j < lst[i].length; j++){
      if(lst[i][j] === x) {
        result.push([i, j]);
      }
    }
  }
  
  result.sort((a, b) => {
    if(a[0] === b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });
  
  return result;
};

console.log(getRow([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
   ], 1)); //  [ [ 0, 0 ], [ 0, 1 ], [ 0, 2 ], [ 0, 3 ], [ 0, 4 ], [ 0, 5 ], [ 1, 4 ], [ 1, 0 ], [ 1, 5 ], [ 2, 0 ], [ 2, 5 ] ]
console.log(getRow([], 1)); // []
console.log(getRow([[], [1], [1, 2, 3]], 3)); // [ [ 2, 2 ] ]


In the code above, I iterate through the given list and find the x and push their coordinates to the result list. Then, I sort the result list first by rows in ascending order and then by columns in descending order.
*/























































































































