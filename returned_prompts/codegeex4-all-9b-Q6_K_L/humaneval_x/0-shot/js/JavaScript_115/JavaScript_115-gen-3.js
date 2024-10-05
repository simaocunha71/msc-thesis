```python
const maxFill = (grid, capacity) => {
  let count = 0
  for (let i = 0; i < grid.length; i++) {
    let j = 0
    while (j < grid[i].length) {
      if (grid[i][j] === 1) {
        count += Math.ceil(grid[i][j] / capacity)
        grid[i][j] = 0
      }
      j++
    }
  }
  return count
}
```
