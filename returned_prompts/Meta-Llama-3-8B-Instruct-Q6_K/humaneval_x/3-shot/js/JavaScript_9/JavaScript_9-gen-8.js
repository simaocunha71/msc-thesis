  let max = numbers[0];
  let result = [max];
  for (let i = 1; i < numbers.length; i++) {
    max = Math.max(max, numbers[i]);
    result.push(max);
  }
  return result;
}



