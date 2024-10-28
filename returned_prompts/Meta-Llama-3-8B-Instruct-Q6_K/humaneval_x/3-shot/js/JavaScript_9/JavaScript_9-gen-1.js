  var result = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > result[result.length - 1]) {
      result.push(numbers[i]);
    } else {
      result.push(result[result.length - 1]);
    }
  }
  return result;
}