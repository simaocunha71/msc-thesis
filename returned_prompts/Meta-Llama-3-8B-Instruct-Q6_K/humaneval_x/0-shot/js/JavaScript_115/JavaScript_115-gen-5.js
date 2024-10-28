Here is the solution using JavaScript:

```javascript
const maxFill = (grid, capacity) => {
    let totalWater = 0;
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[i].length; j++) {
            if(grid[i][j] === 1) {
                totalWater += 1;
            }
        }
    }
    return Math.ceil(totalWater / capacity);
}
```

This function calculates the total amount of water in the grid by iterating over each cell. It then calculates the number of times the bucket needs to be lowered by dividing the total water by the bucket capacity and rounding up to the nearest whole number using the `Math.ceil` function. 

You can use this function to solve the problem as follows:

```javascript
console.log(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)); // Output: 6
console.log(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)); // Output: 5
console.log(maxFill([[0,0,0], [0,0,0]], 5)); // Output: 0
``` 