  let minDiff = Infinity;
  let result = [null, null];

  numbers.sort((a, b) => a - b);

  for  (let i = 0; i < numbers.length - 1; i++) {
    let diff = numbers[i + 1] - numbers[i];
    if  (diff < minDiff) {
      minDiff = diff;
      result = [numbers[i], numbers[i + 1]];
    }
  }

  return result;
}



