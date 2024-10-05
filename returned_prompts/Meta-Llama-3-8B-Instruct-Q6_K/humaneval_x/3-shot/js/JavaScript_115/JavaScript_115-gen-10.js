  let total = 0;
  for (const row of grid) {
    for (const cell of row) {
      total += cell;
    }
  }
  return Math.ceil(total / capacity);
}