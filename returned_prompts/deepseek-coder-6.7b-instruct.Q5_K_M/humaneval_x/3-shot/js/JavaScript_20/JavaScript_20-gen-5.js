  let minDiff = Number.MAX_VALUE;
  let result;

  for  (let i = 0; i < numbers.length; i++) {
    for  (let j = i + 1; j < numbers.length; j++) {
      let diff = Math.abs(numbers[i] - numbers[j]);
      if  (diff < minDiff) {
        minDiff = diff;
        result = [numbers[i], numbers[j]];
      }
    }
  }

  return result.sort((a, b) => a - b);
}



