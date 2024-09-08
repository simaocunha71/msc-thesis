  const result = [];
  let currentMax = numbers[0];

  for (const n of numbers) {
    currentMax = Math.max(currentMax, n);
    result.push(currentMax);
  }

  return result;
}



