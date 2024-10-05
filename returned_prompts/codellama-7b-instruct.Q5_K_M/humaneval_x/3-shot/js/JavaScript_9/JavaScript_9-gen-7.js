  var result = [];
  for (let i = 0; i < numbers.length; i++) {
    var current_max = numbers[i];
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[j] > current_max) {
        current_max = numbers[j];
      }
    }
    result.push(current_max);
  }
  return result;
}



