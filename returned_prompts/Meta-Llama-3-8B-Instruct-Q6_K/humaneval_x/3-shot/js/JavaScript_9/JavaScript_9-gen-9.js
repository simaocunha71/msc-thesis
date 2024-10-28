  let result = [];
  let max = numbers[0];
  for (let i = 0; i < numbers.length; i++) {
    result.push(Math.max(max, numbers[i]));
    max = Math.max(max, numbers[i]);
  }
  return result;
}