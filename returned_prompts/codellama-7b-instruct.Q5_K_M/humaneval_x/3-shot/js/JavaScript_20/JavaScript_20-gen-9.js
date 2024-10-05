  var closest_pair = [];
  var min_distance = Number.MAX_VALUE;

  for (let i = 0; i < numbers.length - 1; i++) {
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



