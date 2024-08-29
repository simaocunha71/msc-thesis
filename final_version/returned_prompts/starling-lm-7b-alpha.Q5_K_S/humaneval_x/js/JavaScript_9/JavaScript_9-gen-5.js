  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    let max = numbers[i];
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[j] > max) {
        max = numbers[j];
      }
      result.push(max);
    }
  }
  return result;
}



