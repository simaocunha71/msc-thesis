const carRaceCollision = (n) => {
  let collisions = 0;

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (i % 2 === 0) {
        if (j % 2 === 1) {
          collisions++;
        }
      } else {
        if (j % 2 === 0) {
          collisions++;
        }
      }
    }
  }
  return collisions;
}

