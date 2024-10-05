
const sumSquares = (lst) => {
  let sum = 0;
  for (let index = 0; index < lst.length; index++) {
    if (index % 3 === 0) {
      sum += lst[index] ** 2;
    } else if (index % 4 === 0) {
      sum += lst[index] ** 3;
    } else {
      sum += lst[index];
    }
  }
  return sum;
};

module.exports = sumSquares;
