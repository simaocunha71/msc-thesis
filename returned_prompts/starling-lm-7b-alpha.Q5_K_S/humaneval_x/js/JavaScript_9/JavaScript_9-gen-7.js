  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    let max = 0;
    for (let j = i; j < numbers.length; j++) {
      max = Math.max(max, numbers[j]);
      result.push(max);
    }
  }
  return result;
}



