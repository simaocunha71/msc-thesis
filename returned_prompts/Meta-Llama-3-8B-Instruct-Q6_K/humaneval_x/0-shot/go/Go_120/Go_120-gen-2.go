  let min_diff = Infinity;
  let closest_pair = [numbers[0], numbers[0]];
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let diff = Math.abs(numbers[i] - numbers[j]);
      if (diff < min_diff) {
        min_diff = diff;
        closest_pair = [Math.min(numbers[i], numbers[j]), Math.max(numbers[i], numbers[j])];
      }
    }
  }
  return closest_pair;
}