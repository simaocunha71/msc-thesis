  let closest_pair = [];
  let closest_distance = Infinity;

  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (Math.abs(numbers[i] - numbers[j]) < closest_distance) {
        closest_distance = Math.abs(numbers[i] - numbers[j]);
        closest_pair = [numbers[i], numbers[j]];
      }
    }
  }

  return closest_pair;
}



