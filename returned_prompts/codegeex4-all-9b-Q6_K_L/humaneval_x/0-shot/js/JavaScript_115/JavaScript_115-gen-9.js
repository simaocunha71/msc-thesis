```python
const maxFill = (grid, capacity) => {
  let sum = 0
  for (let i = 0; i < grid.length; i++) {
    let row_sum = 0
    for (let j = 0; j < grid[i].length; j++) {
      row_sum += grid[i][j]
    }
    sum += Math.ceil(row_sum / capacity)
  }
  return sum
}
```
