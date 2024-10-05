```
const sortArray = (array) => {
  const firstLastSum = array[0] + array[array.length - 1];
  const isOdd = firstLastSum % 2 !== 0;

  return isOdd ? array.slice().sort((a, b) => a - b) : array.slice().sort((a, b) => b - a);
};
``` 