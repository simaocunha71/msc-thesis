  var result = [];
  for (var i = 0; i < numbers.length; i++) {
    if (numbers.indexOf(numbers[i]) == i) {
      result.push(numbers[i]);
    }
  }
  return result;
}



