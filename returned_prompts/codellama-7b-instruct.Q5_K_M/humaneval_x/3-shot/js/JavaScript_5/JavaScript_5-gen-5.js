  var result = [];
  var previous_number = null;
  for (const number of numbers) {
    if (previous_number == null) {
      result.push(number);
    } else {
      result.push(previous_number);
      result.push(delimeter);
      result.push(number);
    }
    previous_number = number;
  }
  return result;
}



