  var min_diff = Number.MAX_VALUE;
  var closest_pair = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let diff = Math.abs(numbers[i] - numbers[j]);
      if (diff < min_diff) {
        min_diff = diff;
        closest_pair = [numbers[i], numbers[j]];
      }
    }
  }

  return closest_pair;
}



