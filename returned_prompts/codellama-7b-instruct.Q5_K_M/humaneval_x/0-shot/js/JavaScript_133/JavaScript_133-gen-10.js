const sumSquares = (lst) => {
  const arr = [];
  for (let i = 0; i < lst.length; i++) {
    arr.push(Math.ceil(lst[i]));
  }
  return arr.reduce((a, b) => a + b * b, 0);
};

