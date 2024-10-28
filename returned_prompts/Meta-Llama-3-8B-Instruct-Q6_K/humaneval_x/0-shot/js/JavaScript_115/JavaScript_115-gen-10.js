Here is the solution to the problem:

```javascript
const maxFill = (grid, capacity) => {
    let count = 0;
    for (let i = 0; i < grid.length; i++) {
        let water = 0;
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === 1) {
                water += 1;
            }
        }
        while (water > 0) {
            water -= capacity;
            count++;
        }
    }
    return count;
};
```

This function iterates over each row of the grid, counts the number of 1's in each row (representing the amount of water in each well), and then empties the well by subtracting the bucket capacity from the water count until the water count is zero. The number of times the bucket is lowered is the total count. The function returns this total count.

For example, for the input `grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]` and `capacity = 1`, the function will return `6`, which is the correct answer. The water in each well is emptied in the following manner:

- Well 1: 1 unit of water -> 0 units of water (1 lowering of the bucket)
- Well 2: 1 unit of water -> 0 units of water (1 lowering of the bucket)
- Well 3: 3 units of water -> 2 units of water (1 lowering of the bucket)
- Well 3: 2 units of water -> 0 units of water (2 lowerings of the bucket)

The total number of lowerings of the bucket is 1 + 1 + 1 + 2 = 6.