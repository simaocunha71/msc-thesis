
//

*/

const carRaceCollision = (n) => {
  let collisions = 0;
  let cars = n;

  // loop through the cars
  for (let i = 0; i < cars; i++) {
    // loop through the cars again
    for (let j = 0; j < cars; j++) {
      // if the cars are the same, skip to next pair
      if (i === j) {
        continue;
      }

      // if the cars are not moving in the same direction
      if (i < j && i > j) {
        continue;
      }

      // if the cars are moving in the same direction
      if (i < j && i === j) {
        collisions++;
      }
    }
  }

  return collisions;
};
