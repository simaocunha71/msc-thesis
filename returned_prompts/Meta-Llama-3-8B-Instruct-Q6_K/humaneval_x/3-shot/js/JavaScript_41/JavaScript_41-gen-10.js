  let collisions = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i != j) {
        let distance = Math.abs(i - j);
        if (distance % 2 == 1) {
          collisions += 1;
        }
      }
    }
  }
  return collisions;
}