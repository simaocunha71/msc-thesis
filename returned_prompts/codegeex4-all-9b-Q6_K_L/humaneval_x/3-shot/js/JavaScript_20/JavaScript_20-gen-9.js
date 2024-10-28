  let min_diff = Infinity;
  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let diff = Math.abs(numbers[i] - numbers[j]);
        if (diff < min_diff) {
          min_diff = diff;
          result = [numbers[i], numbers[j]];
        }
      }
    }
  }
  return result;
}



