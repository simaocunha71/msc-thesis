  let total = 0;
  for (const row of grid) {
    total += row.reduce((a, b) => a + b, 0);
  }
  return Math.ceil(total / capacity);
}
// This solution returns the minimum number of times you need to lower the buckets. It simply calculates the total amount of water and then divides it by the bucket capacity, rounding up to the nearest whole number. This is because you need to fill each bucket at least once to hold the total amount of water.