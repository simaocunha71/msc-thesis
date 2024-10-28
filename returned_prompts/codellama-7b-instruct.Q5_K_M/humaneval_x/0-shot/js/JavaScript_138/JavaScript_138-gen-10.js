const isEqualToSumEven = (n) => {
  const isEven = num => num % 2 === 0;
  const isSumOfFour = num => num % 4 === 0;
  return isSumOfFour(n) && isEven(n);
};

