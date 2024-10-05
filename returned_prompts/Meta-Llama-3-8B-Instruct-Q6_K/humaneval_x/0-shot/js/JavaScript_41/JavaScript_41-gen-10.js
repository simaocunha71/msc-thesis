Here is the solution for the problem:
```
const carRaceCollision = (n) => {
  let collisions = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i !== j && Math.abs(i - j) % (i + j) === 0) {
        collisions++;
      }
    }
  }
  return collisions;
};
```
Explanation:
The problem is to find the number of collisions between cars moving left to right and right to left. Since the cars are infinitely sturdy, we can focus on the relative positions of the cars at any given time.

The key observation is that two cars will collide if and only if their relative distance is a multiple of their sum. This is because the cars are moving at the same speed, so the relative distance between them will increase by their sum at each time step.

We can use two nested loops to iterate over all possible pairs of cars. For each pair, we check if their relative distance is a multiple of their sum. If it is, we increment the collision count.

Finally, we return the total number of collisions.

For example, if there are 3 cars moving left to right and 3 cars moving right to left, the possible collisions are:
```
Car 1 (LR) vs Car 2 (RL)
Car 2 (LR) vs Car 3 (RL)
Car 3 (LR) vs Car 1 (RL)
Car 1 (LR) vs Car 3 (RL)
```
So the output would be 3.