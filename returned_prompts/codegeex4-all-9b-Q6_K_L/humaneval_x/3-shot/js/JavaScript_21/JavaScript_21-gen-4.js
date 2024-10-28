  let min = numbers[0];
  let max = numbers[0];

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] < min) {
      min = numbers[i];
    } else if (numbers[i] > max) {
      max = numbers[i];
    }
  }

  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    result.push((numbers[i] - min) / (max - min));
  }

  return result;
}