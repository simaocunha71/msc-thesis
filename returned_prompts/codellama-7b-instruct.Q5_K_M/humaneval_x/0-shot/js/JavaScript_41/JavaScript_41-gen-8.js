const carRaceCollision = (n) => {
  let collisions = 0;
  const leftToRight = [];
  const rightToLeft = [];

  for (let i = 0; i < n; i++) {
    leftToRight[i] = i;
    rightToLeft[i] = i;
  }

  while (leftToRight.length > 0 && rightToLeft.length > 0) {
    const l = leftToRight.pop();
    const r = rightToLeft.pop();
    if (l < r) {
      leftToRight.push(l);
      leftToRight.push(r);
    } else if (l > r) {
      rightToLeft.push(l);
      rightToLeft.push(r);
    } else {
      collisions++;
    }
  }

  return collisions;
};
