  let min_diff = Infinity;
  let first_closest = null;
  let second_closest = null;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let diff = Math.abs(numbers[i] - numbers[j]);
        if (diff < min_diff) {
          min_diff = diff;
          first_closest = numbers[i];
          second_closest = numbers[j];
        }
      }
    }
  }

  return [first_closest, second_closest];
}



