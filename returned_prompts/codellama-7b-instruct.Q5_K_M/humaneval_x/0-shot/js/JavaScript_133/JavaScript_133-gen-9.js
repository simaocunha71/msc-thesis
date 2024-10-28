const sumSquares = (lst) => {
  let roundedLst = lst.map(num => Math.ceil(num));
  let result = roundedLst.map(num => num ** 2).reduce((a, b) => a + b);
  return result;
}


