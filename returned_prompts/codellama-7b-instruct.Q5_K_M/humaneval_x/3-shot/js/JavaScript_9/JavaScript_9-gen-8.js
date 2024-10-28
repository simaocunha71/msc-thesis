  var result = [];
  var current_max = numbers[0];
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > current_max) {
      current_max = numbers[i];
    }
    result.push(current_max);
  }
  return result;
}



