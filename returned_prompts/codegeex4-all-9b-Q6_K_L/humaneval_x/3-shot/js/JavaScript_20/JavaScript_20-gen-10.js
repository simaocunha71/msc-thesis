  let minDifference = Infinity;
  let pair = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let difference = Math.abs(numbers[i] - numbers[j]);
      if (difference < minDifference) {
        minDifference = difference;
        pair = [numbers[i], numbers[j]];
      }
    }
  }

  return pair;
}



