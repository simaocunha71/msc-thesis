  var min_value = numbers[0];
  var max_value = numbers[0];

  for (const number of numbers) {
    if (number < min_value) {
      min_value = number;
    }
    if (number > max_value) {
      max_value = number;
    }
  }

  var result = [];
  for (const number of numbers) {
    result.push((number - min_value) / (max_value - min_value));
  }

  return result;
}



