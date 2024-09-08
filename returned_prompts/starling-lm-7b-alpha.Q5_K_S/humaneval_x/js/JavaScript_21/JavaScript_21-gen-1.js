  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  let range = max - min;

  return numbers.map(x => {
    return ((x - min) / range);
  });
}



