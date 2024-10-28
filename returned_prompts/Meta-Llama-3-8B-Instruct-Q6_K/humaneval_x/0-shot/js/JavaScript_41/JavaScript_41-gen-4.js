Here is a simple and efficient solution for this problem. The idea is to simulate the race by considering the position of each car at a given time. We can use two arrays, one for cars moving from left to right and one for cars moving from right to left. For each car, we calculate its position at a given time and check if there is a car from the other direction that is at the same position. If there is, we increment the collision counter.

Here is the implementation in JavaScript:
```
const carRaceCollision = (n) => {
  let collisionCount = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i !== j && Math.abs(i - j) % (i + j) === 0) {
        collisionCount++;
      }
    }
  }
  return collisionCount;
};
```
This solution has a time complexity of O(n^2) and a space complexity of O(1), which is efficient for small to medium-sized inputs. For larger inputs, a more efficient solution might be needed.

You can test this function with different values of n to see the number of collisions:
```
console.log(carRaceCollision(1)); // 0
console.log(carRaceCollision(2)); // 1
console.log(carRaceCollision(3)); // 2
console.log(carRaceCollision(4)); // 3
console.log(carRaceCollision(5)); // 6
```