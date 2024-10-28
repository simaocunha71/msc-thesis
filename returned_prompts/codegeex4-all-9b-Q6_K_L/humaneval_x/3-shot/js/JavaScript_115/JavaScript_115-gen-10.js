  let total_wells = grid.length * grid[0].length;
  let wells_filled = 0;
  let buckets_used = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == 1) {
        wells_filled += 1;
        buckets_used += Math.ceil(wells_filled / capacity);
      }
    }
  }

  return buckets_used;
}



