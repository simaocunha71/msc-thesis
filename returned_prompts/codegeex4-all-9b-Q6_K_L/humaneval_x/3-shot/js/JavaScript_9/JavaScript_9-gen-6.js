  var max = numbers[0];
  var result = [];

  for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    result.push(max);
  }

  return result;
}



