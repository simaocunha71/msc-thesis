  let min_diff = Number.MAX_SAFE_INTEGER;
  let min_index = 0;
  let min_index2 = 0;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let diff = Math.abs(numbers[i] - numbers[j]);
        if (diff < min_diff) {
          min_diff = diff;
          min_index = i;
          min_index2 = j;
        }
      }
    }
  }

  return (numbers[min_index], numbers[min_index2]);
}



