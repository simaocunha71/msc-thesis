  const min = Math.min(...numbers);
  const max = Math.max(...numbers);

  return numbers.map(x => (x - min) / (max - min));
}



