  let result = [];
  let index = 0;
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] != numbers[index]) {
      result[index++] = numbers[i];
    }
  }
  return result;
}



