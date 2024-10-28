  let result = 0;
  for (const row of grid) {
    let current_sum = 0;
    for (const well of row) {
      if (well == 1) {
        current_sum += 1;
      } else {
        result += Math.ceil(current_sum / capacity);
        current_sum = 0;
      }
    }
    result += Math.ceil(current_sum / capacity);
  }
  return result;
}