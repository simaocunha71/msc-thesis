  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(n => (n - min) / (max - min));
}


