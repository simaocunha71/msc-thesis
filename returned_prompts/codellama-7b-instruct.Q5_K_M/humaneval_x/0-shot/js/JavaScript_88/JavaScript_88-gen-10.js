const sortArray = array => {
  const result = array.sort((a, b) => a - b);
  const sum = result[0] + result[result.length - 1];
  return sum % 2 ? result : result.reverse();
};

// test cases
console.log(sortArray([2, 4, 3, 0, 1, 5]));
console.log(sortArray([2, 4, 3, 0, 1, 5, 6]));
