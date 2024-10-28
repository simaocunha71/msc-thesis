  let closest_pair = [numbers[0], numbers[0]];
  let min_distance = Infinity;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < min_distance) {
        min_distance = distance;
        closest_pair = [Math.min(numbers[i], numbers[j]), Math.max(numbers[i], numbers[j])];
      }
    }
  }

  return closest_pair;
}