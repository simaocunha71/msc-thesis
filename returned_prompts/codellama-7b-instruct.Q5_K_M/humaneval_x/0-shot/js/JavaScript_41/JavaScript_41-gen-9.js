  const collisions = 0;

  for (let i = 0; i < n; i++) {
    const leftToRight = i;
    const rightToLeft = n - i - 1;
    if (leftToRight === rightToLeft) {
      continue;
    }
    collisions++;
  }
  return collisions;
}

