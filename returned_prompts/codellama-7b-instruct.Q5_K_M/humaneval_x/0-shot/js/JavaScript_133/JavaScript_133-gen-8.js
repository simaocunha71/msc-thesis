const sumSquares = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    sum += Math.pow(Math.ceil(lst[i]), 2);
  }
  return sum;
};

B:
const sumSquares = (lst) => {
  return lst.map(Math.ceil)
    .map(x => x * x)
    .reduce((acc, cur) => acc + cur);
};

C:
const sumSquares = (lst) => {
  const squared = lst.map(x => x * x);
  const ceil = lst.map(Math.ceil);
  const sum = squared.map((x, i) => x * ceil[i]).reduce((a, b) => a + b);
  return sum;
};

D:
const sumSquares = (lst) => {
  return lst.map(x => Math.pow(Math.ceil(x), 2)).reduce((a, b) => a + b);
};

E:
const sumSquares = (lst) => {
  return lst.map(x => Math.ceil(x)).map(x => x * x).reduce((a, b) => a + b);
};

F:
const sumSquares = (lst) => {
  return lst.map(x => x * x).map(x => Math.ceil(x)).reduce((a, b) => a + b);
};
