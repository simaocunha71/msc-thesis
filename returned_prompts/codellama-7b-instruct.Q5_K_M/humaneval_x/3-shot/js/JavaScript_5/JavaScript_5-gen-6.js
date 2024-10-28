  let result = [];
  let size = numbers.length;
  for (let i = 0; i < size; i++) {
    result.push(numbers[i]);
    if (i < size - 1) {
      result.push(delimeter);
    }
  }
  return result;
}



