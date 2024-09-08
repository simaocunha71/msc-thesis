  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(n => {
    return (n - min) / (max - min);
  });
}



