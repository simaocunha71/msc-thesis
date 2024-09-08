  let num_wells = grid.length;
  let num_units = grid[0].reduce((a, b) => a + b);
  let num_buckets = Math.ceil(num_units / capacity);

  let water_remaining = num_units;
  let buckets_used = 0;
  while (water_remaining > 0) {
    let bucket_amount = Math.min(water_remaining, capacity);
    water_remaining -= bucket_amount;
    buckets_used += 1;
  }
  return buckets_used;
}



