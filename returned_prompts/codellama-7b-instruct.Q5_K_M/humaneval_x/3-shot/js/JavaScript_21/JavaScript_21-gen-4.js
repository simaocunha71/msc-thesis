  var min = numbers[0];
  var max = numbers[0];

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < min) {
      min = numbers[i];
    }
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }

  var result = [];
  for (let i = 0; i < numbers.length; i++) {
    result.push((numbers[i] - min) / (max - min));
  }

  return result;
}



