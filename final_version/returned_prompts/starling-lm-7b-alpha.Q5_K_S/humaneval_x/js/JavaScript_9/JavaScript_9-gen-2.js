  let result = [];
  let max = numbers[0];

  for (let i = 0; i < numbers.length; i++) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    result.push(max);
  }

  return result;
}



