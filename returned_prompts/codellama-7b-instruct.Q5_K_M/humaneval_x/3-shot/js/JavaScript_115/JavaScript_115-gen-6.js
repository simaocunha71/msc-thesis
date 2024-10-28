  const row_length = grid[0].length;

  let total_water = 0;
  let max_water = 0;

  for (let i = 0; i < row_length; i++) {
    let current_water = 0;
    for (let j = 0; j < grid.length; j++) {
      if (grid[j][i] == 1) {
        current_water += 1;
      }
    }
    if (current_water > max_water) {
      max_water = current_water;
    }
    total_water += current_water;
  }

  if (total_water <= capacity) {
    return 0;
  }

  // bucket_count -> number of buckets
  // bucket_height -> maximum height of water that can be filled in a single bucket
  // bucket_height -> sum of all heights of water in a single bucket
  let bucket_count = 0;
  let bucket_height = 0;
  let bucket_sum = 0;
  while (max_water > capacity) {
    bucket_count += 1;

    // bucket_height -> maximum height of water that can be filled in a single bucket
    bucket_height = max_water;
    // bucket_sum -> sum of all heights of water in a single bucket
    bucket_sum = 0;
    for (let i = 0; i < row_length; i++) {
      if (grid[i][bucket_count - 1] == 1) {
        bucket_sum += 1;
      }
    }
    max_water -= bucket_height;
  }
  return bucket_count;
}



