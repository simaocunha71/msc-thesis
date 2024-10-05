const sortArray = (array) => {
  const sum = array.reduce((acc, curr) => acc + curr);
  const sortedArray = array.sort((a, b) => a - b);
  const result = sum % 2 === 0 ? sortedArray.reverse() : sortedArray;
  return result;
};