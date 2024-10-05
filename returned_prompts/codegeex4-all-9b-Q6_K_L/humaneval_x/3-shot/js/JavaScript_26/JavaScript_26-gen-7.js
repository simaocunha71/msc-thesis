  var result = [];
  for (var i = 0; i < numbers.length; i++) {
    if (result.indexOf(numbers[i]) == -1) {
      result.push(numbers[i]);
    }
  }
  return result;
}



