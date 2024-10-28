  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  return numbers.map(num => (num - min) / (max - min));
}