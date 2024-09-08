  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    if (i != 0) {
      result.push(delimeter);
    }
    result.push(numbers[i]);
  }

  return result;
}



