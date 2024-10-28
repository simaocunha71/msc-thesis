  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  let result = [];

  for (const n of numbers) {
    result.push((n - min) / (max - min));
  }

  return result;
}



