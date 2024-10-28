  let count = 0;
  for (let row of grid) {
    let water = 0;
    for (let cell of row) {
      if (cell) {
        water += cell;
      }
    }
    count += Math.ceil(water / capacity);
  }
  return count;
}