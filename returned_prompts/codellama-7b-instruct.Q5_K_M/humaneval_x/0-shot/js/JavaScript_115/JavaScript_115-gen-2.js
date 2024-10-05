  /*
    Input: 
        grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        bucket_capacity : 1
    Output: 6

    Input: 
        grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        bucket_capacity : 2
    Output: 5
  
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
  let rows = grid.length
  let cols = grid[0].length
  let max = 0
  let min = 1000
  let buckets = []
  let wells = []

  for (let i = 0; i < rows; i++) {
    let well = []
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] == 1) {
        well.push(j)
      }
    }
    if (well.length > max) {
      max = well.length
    }
    if (well.length < min) {
      min = well.length
    }
  }

  // all wells have same length, so we can divide all wells by min and get the number of times
  // we need to lower the bucket
  let times = Math.floor(max / min)
  let remaining = max % min
  let bucket = remaining

  // remaining is the number of times we need to use a bucket, so we need to add the number of times
  // we need to use the bucket
  if (remaining > 0) {
    times = times + bucket