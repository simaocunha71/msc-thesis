  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    result[i] = (numbers[i] - min) / (max - min);
  }
  return result;
}



