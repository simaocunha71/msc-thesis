const sortArray = (array) => {
  const result = array.sort((a, b) => {
    if (a + b % 2 === 0) {
      return b - a;
    } else {
      return a - b;
    }
  });
  return result;
};

console.log(sortArray([]), []);
console.log(sortArray([5]), [5]);
console.log(sortArray([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5]);
console.log(sortArray([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0]);
console.log(sortArray([1, 1, 1, 1]), [1, 1, 1, 1]);
