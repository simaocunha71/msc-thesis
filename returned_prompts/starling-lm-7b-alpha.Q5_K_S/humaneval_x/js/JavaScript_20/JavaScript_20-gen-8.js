  let min_difference = Number.MAX_SAFE_INTEGER;
  let min_a = 0;
  let min_b = 0;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (Math.abs(numbers[i] - numbers[j]) < min_difference) {
        min_difference = Math.abs(numbers[i] - numbers[j]);
        min_a = i;
        min_b = j;
      }
    }
  }

  return [numbers[min_a], numbers[min_b]];
}



