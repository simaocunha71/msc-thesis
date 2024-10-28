  let totalWater = 0;
  let wells = grid.length;
  let bucketsNeeded = 0;

  for (let i = 0; i < wells; i++) {
    totalWater += grid[i].reduce((acc, val) => acc + val, 0);
  }

  while (totalWater > 0) {
    bucketsNeeded++;
    totalWater -= capacity;
  }

  return bucketsNeeded;
}...



