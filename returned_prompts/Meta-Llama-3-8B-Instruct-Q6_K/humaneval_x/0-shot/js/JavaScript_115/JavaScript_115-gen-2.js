Here is a JavaScript solution for the problem:

```javascript
const maxFill = (grid, capacity) => {
    let count = 0;
    let filled = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === 1) {
                filled += 1;
            }
        }
    }
    while (filled > 0) {
        let filledThisRound = 0;
        for (let i = 0; i < grid.length; i++) {
            for (let j = 0; j < grid[i].length; j++) {
                if (grid[i][j] === 1 && filled > 0) {
                    grid[i][j] = 0;
                    filled--;
                    filledThisRound++;
                }
            }
        }
        count++;
    }
    return count;
};
```

In this solution, we first calculate the total number of units of water in the wells. Then, we enter a loop where we keep filling the buckets until there is no more water in the wells. We keep track of the number of times we have to lower the buckets, and return this number at the end.

This solution has a time complexity of O(m * n), where m is the number of rows and n is the number of columns in the grid. This is because we need to iterate over each cell in the grid to calculate the total number of units of water and to fill the buckets. The space complexity is O(1), as we only use a constant amount of space to store the count and the filled variable. 