const doubleTheDifference = (lst) => {
  if (lst.length === 0) return 0;

  const oddSquares = lst.filter(x => x % 2 !== 0 && x >= 0)
    .map(x => x * x);

  return oddSquares.reduce((a, b) => a + b, 0);
}