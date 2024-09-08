  let result = [];
  let currentMax = numbers[0];

  for (let i = 0; i < numbers.length; i++) {
    result.push(currentMax);
    currentMax = Math.max(currentMax, numbers[i]);
  }

  return result;
}



