  let result = [];
  let current_max = numbers[0];

  for (const n of numbers) {
    current_max = Math.max(current_max, n);
    result.push(current_max);
  }
  return result;
}



