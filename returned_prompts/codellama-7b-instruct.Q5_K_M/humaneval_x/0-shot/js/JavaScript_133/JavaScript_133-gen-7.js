const sumSquares = (lst) => {
  const ceilList = lst.map(i => Math.ceil(i));
  return ceilList.reduce((a,b) => a + b * b, 0);
}
