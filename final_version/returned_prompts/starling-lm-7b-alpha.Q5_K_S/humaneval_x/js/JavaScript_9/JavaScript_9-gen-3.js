  let result = [];
  let max = numbers[0];
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      result.push(numbers[i]);
      max = numbers[i];
    } else {
      result.push(max);
    }
  }
  return result;
}



