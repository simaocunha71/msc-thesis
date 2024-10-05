  let minDistance = Infinity;
  let pair = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let distance = Math.abs(numbers[i] - numbers[j]);
        if (distance < minDistance) {
          minDistance = distance;
          pair = [Math.min(numbers[i], numbers[j]), Math.max(numbers[i], numbers[j])];
        }
      }
    }
  }

  return pair;
}