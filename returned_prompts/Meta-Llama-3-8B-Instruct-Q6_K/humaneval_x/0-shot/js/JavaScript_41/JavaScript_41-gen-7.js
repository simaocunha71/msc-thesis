Here is a JavaScript solution for the problem:

```javascript
const carRaceCollision = (n) => {
    let collisions = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i !== j) {
                if (Math.floor((i - j) / (n - 1)) === 0 || Math.floor((i - j) / (n - 1)) === 1) {
                    collisions++;
                }
            }
        }
    }
    return collisions;
};
```

The function `carRaceCollision` takes an integer `n` as an argument, which represents the number of cars moving left to right and the number of cars moving right to left. The function returns the number of collisions.

The function uses two nested loops to iterate over all pairs of cars. It checks if the distance between the two cars is a multiple of the distance between two consecutive cars. If it is, then the cars will collide. The function increments the `collisions` variable each time a collision is found. Finally, the function returns the total number of collisions.

Note: The function assumes that the cars are evenly spaced and that there are no gaps between the cars. It also assumes that the cars are moving at the same speed. The function uses the `Math.floor` function to convert the distance between the cars to an integer, which is used to determine if the cars will collide. If the distance is a multiple of the distance between two consecutive cars, then the cars will collide. Otherwise, they will not collide. The function returns the total number of collisions.