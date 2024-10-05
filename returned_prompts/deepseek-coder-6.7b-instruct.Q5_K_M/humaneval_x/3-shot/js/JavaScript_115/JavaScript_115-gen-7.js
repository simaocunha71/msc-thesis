  let total_wells = grid.length * grid[0].length;
  let total_water = grid.reduce((a, b) => a.concat(b)).reduce((a, b) => a + b);
  return Math.ceil(total_water / capacity);
}



