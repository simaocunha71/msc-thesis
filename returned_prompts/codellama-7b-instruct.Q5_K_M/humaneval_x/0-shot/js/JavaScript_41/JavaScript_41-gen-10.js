  const leftToRightCars = [];
  const rightToLeftCars = [];
  let totalCollisions = 0;

  for (let i = 0; i < n; i++) {
    leftToRightCars.push(i);
    rightToLeftCars.push(i);
  }

  const carCollision = (car, otherCar) => {
    leftToRightCars[car] = null;
    rightToLeftCars[otherCar] = null;
    totalCollisions++;
  }

  while (leftToRightCars.length > 0 && rightToLeftCars.length > 0) {
    for (let i = 0; i < leftToRightCars.length; i++) {
      if (leftToRightCars[i] === null) continue;
      for (let j = rightToLeftCars.length - 1; j >= 0; j--) {
        if (rightToLeftCars[j] === null) continue;
        if (leftToRightCars[i] < rightToLeftCars[j]) {
          carCollision(i, j);
        }
      }
    }
  }

  return totalCollisions;
}

