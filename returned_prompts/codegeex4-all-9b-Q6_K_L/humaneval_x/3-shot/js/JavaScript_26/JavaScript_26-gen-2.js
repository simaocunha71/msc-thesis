  var result = [];
  for (let i = 0; i < numbers.length; i++) {
    if (!result.includes(numbers[i])) {
      result.push(numbers[i]);
    }
  }
  return result;
}



