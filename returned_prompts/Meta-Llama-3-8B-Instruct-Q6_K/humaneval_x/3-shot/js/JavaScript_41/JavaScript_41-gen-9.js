  let collisions = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i != j) {
        let diff = Math.abs(i - j);
        if (diff % 2 == 1) {
          collisions++;
        }
      }
    }
  }
  return collisions;
}