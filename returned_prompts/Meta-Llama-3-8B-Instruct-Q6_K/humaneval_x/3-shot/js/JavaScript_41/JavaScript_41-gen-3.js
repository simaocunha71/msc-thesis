  let collisions = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i != j) {
        if (i + j == n + 1) {
          collisions++;
        }
      }
    }
  }
  return collisions;
}