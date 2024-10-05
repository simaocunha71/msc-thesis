  var result = [];
  result.push(numbers[0]);
  for (let i = 1; i < numbers.length; i++) {
    result.push(Math.max(numbers[i], result[i - 1]));
  }
  return result;
}



