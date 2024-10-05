The function `carRaceCollision` can be implemented as follows:

```javascript
const carRaceCollision = (n) => {
  // The number of collisions is always n because each car moving left to right
  // will collide with each car moving right to left.
  return n;
};
```

This function simply returns the value of `n`, which represents the number of collisions that will occur.