  let min = Infinity;
  let min_a = 0;
  let min_b = 0;
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let d = Math.abs(numbers[i] - numbers[j]);
      if (d < min) {
        min = d;
        min_a = i;
        min_b = j;
      }
    }
  }
  return [numbers[min_a], numbers[min_b]];
}



