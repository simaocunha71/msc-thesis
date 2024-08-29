  let min = Infinity;
  let candidates = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j && Math.abs(numbers[i] - numbers[j]) < min) {
        min = Math.abs(numbers[i] - numbers[j]);
        candidates = [numbers[i], numbers[j]];
      }
    }
  }

  return candidates;
}



