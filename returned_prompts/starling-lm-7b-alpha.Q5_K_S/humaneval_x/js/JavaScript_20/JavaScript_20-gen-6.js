  let closest_pair = [];
  let min_distance = Infinity;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < min_distance) {
        min_distance = distance;
        closest_pair = [numbers[i], numbers[j]];
      }
    }
  }

  return closest_pair;
}



