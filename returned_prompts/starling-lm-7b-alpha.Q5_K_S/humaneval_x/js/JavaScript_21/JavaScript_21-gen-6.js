  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  return numbers.map(n => (n - min) / (max - min));
}



