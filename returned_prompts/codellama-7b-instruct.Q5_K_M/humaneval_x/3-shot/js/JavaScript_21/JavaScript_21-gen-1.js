  let min_val = Math.min(...numbers);
  let max_val = Math.max(...numbers);
  let range = max_val - min_val;

  return numbers.map((x) => {
    return (x - min_val) / range;
  });
}



