```python
const maxFill = (grid, capacity) => {
    let ans = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === 1) {
                ans += Math.ceil(grid[i].length / capacity);
            }
        }
    }
    return ans;
};
```
