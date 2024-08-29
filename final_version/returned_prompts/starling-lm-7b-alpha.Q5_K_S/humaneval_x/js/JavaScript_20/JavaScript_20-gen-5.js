  let min = Number.POSITIVE_INFINITY;
  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let d = Math.abs(numbers[i] - numbers[j]);
      if (d < min) {
        min = d;
        result = [numbers[i], numbers[j]];
      }
    }
  }

  return result;
}



