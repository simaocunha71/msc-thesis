  var result = [];
  var last_index = numbers.length - 1;

  for (var i = 0; i < numbers.length; i++) {
    result.push(numbers[i]);
    if (i < last_index) {
      result.push(delimeter);
    }
  }

  return result;
}



