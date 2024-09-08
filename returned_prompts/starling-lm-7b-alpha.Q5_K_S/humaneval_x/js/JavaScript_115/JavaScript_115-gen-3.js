  let total_water = 0;
  for (const row of grid) {
    total_water += row.reduce((a, b) => a + b);
  }
  return Math.ceil(total_water / capacity);
}



