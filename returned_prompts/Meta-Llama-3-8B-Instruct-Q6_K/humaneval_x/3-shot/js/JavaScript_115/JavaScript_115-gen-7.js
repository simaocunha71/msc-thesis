  let count = 0;
  for (const row of grid) {
    let water = 0;
    for (const cell of row) {
      if (cell == 1) {
        water += 1;
      }
    }
    while (water > 0) {
      let filled = Math.min(water, capacity);
      water -= filled;
      count += 1;
    }
  }
  return count;
}