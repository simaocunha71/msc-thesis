
const sumSquares = (lst) => {
  let result = 0;
  for(let i of lst) {
    i = Math.ceil(i);
    result += i * i;
  }
  return result;
};

B:

const sumSquares = (lst) => {
  let result = 0;
  for(let i of lst) {
    result += Math.pow(Math.ceil(i), 2);
  }
  return result;
};

C:

const sumSquares = (lst) => {
  return lst.map(Math.ceil).map(i => i * i).reduce((a, b) => a + b);
};

D:

const sumSquares = (lst) => {
  return Math.ceil(lst.reduce((a, b) => a + b, 0));
};

E:

const sumSquares = (lst) => {
  return Math.ceil(lst.reduce((a, b) => a + b * b, 0));
};
