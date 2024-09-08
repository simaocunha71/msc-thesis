  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    if (i == 0) {
      result.push(numbers[i]);
    } else {
      result.push(numbers[i], delimeter);
    }
  }
  return result;
}



