  var result = [numbers[0]];
  for (var i = 1; i < numbers.length; i++) {
    result.push(Math.max(result[i - 1], numbers[i]));
  }
  return result;
}