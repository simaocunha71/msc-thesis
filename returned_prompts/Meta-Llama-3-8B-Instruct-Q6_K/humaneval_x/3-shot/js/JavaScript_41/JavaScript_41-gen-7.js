  let collisions = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i != j) {
        if (i >= j) {
          collisions++;
        }
      }
    }
  }
  return collisions;
}
// or
const carRaceCollision = (n) => {
  return Math.comb(n, 2);
}
// where Math.comb(n, 2) is the combination of n items taken 2 at a time.
// This is the number of pairs of distinct cars that can collide.