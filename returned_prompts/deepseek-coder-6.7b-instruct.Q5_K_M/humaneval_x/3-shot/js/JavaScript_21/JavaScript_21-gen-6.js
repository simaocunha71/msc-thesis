  let min 		=  Math.min(...numbers);
  let max 		=  Math.max(...numbers);
  let range 		=  max - min;
  return numbers.map((n) => (n - min) / range);
}



