const sumSquares = (lst) => {
  const roundedList = lst.map(num => Math.ceil(num));
  return roundedList.map(num => num ** 2).reduce((acc, curr) => acc + curr);
}
