  var closest_pair = [];
  var closest_distance = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      var distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < closest_distance) {
        closest_distance = distance;
        closest_pair = [numbers[i], numbers[j]];
      }
    }
  }

  return closest_pair;
}



