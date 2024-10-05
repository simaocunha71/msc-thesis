  var result = [];
  var current_distance = Infinity;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let distance = Math.abs(numbers[i] - numbers[j]);
        if (distance < current_distance) {
          current_distance = distance;
          result = [numbers[i], numbers[j]];
        }
      }
    }
  }

  return result;
}