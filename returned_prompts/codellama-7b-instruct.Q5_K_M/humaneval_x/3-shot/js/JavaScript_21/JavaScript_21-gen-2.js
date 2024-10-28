  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const range = max - min;

  return numbers.map(n => (n - min) / range);
}



