/*
  Time complexity : O(n)
  Space complexity : O(n)

  We are using a queue to keep track of the positions of the wells that still need to be filled.
  We start the queue with the positions of the wells that have the most water (the first row).
  We then dequeue the top position of the queue, and check the position of the well we are about to fill.
  If it is not the last row, we enqueue the position of the well that is below it.
  We then check the position of the well to the right of the one we are about to fill, 
  and we enqueue the position of the well that is to the right of it.
  We repeat this process until the queue is empty.
  */
  const queue = []
  for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[i].length; j++) {
          if (grid[i][j] === 1) {
              queue.push([i, j])
          }
      }
  }
  let fill = 0
  while (queue.length) {
      const [i, j] = queue.shift()
      if (i === grid.length - 1) {
          continue
      }
      if (grid[i + 1][j] === 0) {
          grid[i + 1][j] = 1
          queue.push([i + 1, j])
      }
      if (grid[i + 1][j + 1] === 0 && j + 1 < grid[i].length) {
          grid[i + 1][j + 1] = 1
          queue.push([i + 1, j + 1])
      }
      fill++
  }
  return fill
}
