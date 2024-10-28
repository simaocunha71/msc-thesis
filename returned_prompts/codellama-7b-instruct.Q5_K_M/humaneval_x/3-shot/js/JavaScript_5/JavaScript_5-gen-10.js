  var result = [];
  var last = numbers.length - 1;
  for (var i = 0; i <= last; i++) {
    result.push(numbers[i]);
    if (i < last) {
      result.push(delimeter);
    }
  }
  return result;
}



