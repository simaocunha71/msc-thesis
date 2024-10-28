const sumSquares = lst => {
  let sum = 0;
  let squares = [];
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
      squares[i] = lst[i] ** 2;
    }
    if (i % 4 === 0) {
      squares[i] = lst[i] ** 3;
    }
  }
  for (let j = 0; j < squares.length; j++) {
    sum += squares[j];
  }
  return sum;
};
