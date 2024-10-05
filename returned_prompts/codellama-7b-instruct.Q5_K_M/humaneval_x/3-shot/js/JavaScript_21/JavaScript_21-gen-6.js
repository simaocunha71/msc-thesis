  let min_value = numbers.reduce((a, b) => Math.min(a, b));
  let max_value = numbers.reduce((a, b) => Math.max(a, b));
  let range = max_value - min_value;
  let result = numbers.map((number) => (number - min_value) / range);
  return result;
}



