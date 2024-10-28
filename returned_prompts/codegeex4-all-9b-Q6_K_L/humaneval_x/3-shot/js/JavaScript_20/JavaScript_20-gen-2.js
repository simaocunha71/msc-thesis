  var min_distance = Infinity;
  var min_pair = [null, null];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let distance = Math.abs(numbers[i] - numbers[j]);
        if (distance < min_distance) {
          min_distance = distance;
          min_pair = [numbers[i], numbers[j]];
        }
      }
    }
  }

  return min_pair;
}