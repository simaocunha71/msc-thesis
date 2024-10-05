  const min_val = Math.min(...numbers);
  const max_val = Math.max(...numbers);
  const range = max_val - min_val;
  return numbers.map(n => (n - min_val) / range);
}



