/* From a given list of integers, generate a list of rolling maximum element found until given moment
  in the sequence.
  >>> rollingMax([1, 2, 3, 2, 3, 4, 2])
  [1, 2, 3, 3, 3, 4, 4]
  */
const rollingMax = (numbers) => {
  const currentMax = numbers[0];
  let i = 1;
  while(i < numbers.length - 1 && currentMax <= (numbers[i]) ){
    currentMax = (numbers[i]);
    i++;
  }
  return [...currentMax, ...rollingMax(numbers.slice(i + 1).reverse())];
};
