  if (numbers.length == 0) {
    return numbers;
  }

  let result = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    result.push(delimeter);
    result.push(numbers[i]);
  }
  return result;
}