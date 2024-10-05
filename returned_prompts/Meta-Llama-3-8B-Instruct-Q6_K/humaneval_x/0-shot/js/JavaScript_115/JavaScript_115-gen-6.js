```
const maxFill = (grid, capacity) => {
    let ans = 0;
    for (let i = 0; i < grid.length; i++) {
        let water = 0;
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === 1) {
                water += 1;
            }
        }
        ans += Math.ceil(water / capacity);
    }
    return ans;
};
```
The function `maxFill` takes a grid of wells and a bucket capacity as input. It calculates the number of times the buckets need to be lowered to empty the wells.

The function iterates over each well in the grid. For each well, it calculates the total amount of water in that well and then calculates the number of times the bucket needs to be lowered to empty the well by dividing the amount of water by the bucket capacity and rounding up to the nearest integer using the `Math.ceil` function. The total number of times the buckets need to be lowered is the sum of these calculations for all wells. The function returns this total.

For example, if the input grid is `[[0,0,1,0], [0,1,0,0], [1,1,1,1]]` and the bucket capacity is 1, the function will return 6, because the buckets need to be lowered 2 times for the first well, 1 time for the second well, and 3 times for the third well.