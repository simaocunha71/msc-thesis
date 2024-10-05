  var minDistance = Infinity;
  var result = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < minDistance) {
        minDistance = distance;
        result = [numbers[i], numbers[j]];
      }
    }
  }
  return result;
}