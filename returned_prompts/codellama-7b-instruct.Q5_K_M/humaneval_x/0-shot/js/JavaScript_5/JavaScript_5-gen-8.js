const intersperse = (numbers, delimeter) => numbers.reduce((acc, n, i, arr) => {
  acc.push(n);
  if (i < arr.length - 1) {
    acc.push(delimeter);
  }
  return acc;
}, []);
