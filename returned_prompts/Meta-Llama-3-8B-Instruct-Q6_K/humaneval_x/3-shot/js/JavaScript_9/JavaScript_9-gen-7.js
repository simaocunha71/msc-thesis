  let result = [];
  let maxSoFar = numbers[0];

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > maxSoFar) {
      maxSoFar = numbers[i];
    }
    result.push(maxSoFar);
  }

  return result;
}
