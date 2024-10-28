const doubleTheDifference = (lst) =>
  lst.filter(x => x % 1 === 0 && x >= 0)
    .map(x => x * x)
    .reduce((acc, x) => acc + x, 0);

//B:
const doubleTheDifference = (lst) =>
  lst.filter(x => !isNaN(x) && x % 1 === 0 && x >= 0)
    .map(x => x * x)
    .reduce((acc, x) => acc + x, 0);

//C:
const doubleTheDifference = (lst) =>
  lst.filter(x => x >= 0 && x % 1 === 0)
    .map(x => x * x)
    .reduce((acc, x) => acc + x, 0);

//D:
const doubleTheDifference = (lst) =>
  lst.filter(x => x >= 0 && x % 1 === 0)
    .map(x => x * x)
    .reduce((acc, x) => acc + x, 0);

//E:
const doubleTheDifference = (lst) =>
  lst.filter(x => x >= 0 && x % 1 === 0)
    .map(x => x * x)
    .reduce((acc, x) => acc + x, 0);

//F:
const doubleTheDifference = (lst) =>
  lst.filter(x => x >= 0 && x % 1 === 0)
    .map(x => x * x)
    .reduce((acc, x) => acc + x, 0);

//G:
const doubleTheDifference = (lst) =>
  lst.filter(x => x >= 0 && x % 1 === 0)
    .map(x => x * x)
    .reduce((acc, x) => acc + x, 0);

//H:
const doubleTheDifference = (lst) =>
  lst.filter(x => x >= 0 && x % 1 === 0)
    .map(x => x * x)
    .reduce((acc, x