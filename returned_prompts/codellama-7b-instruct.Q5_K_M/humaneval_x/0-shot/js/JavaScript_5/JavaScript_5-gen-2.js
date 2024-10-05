const intersperse = (numbers, delimeter) => {
  const newNumbers = [];
  for (let i = 0; i < numbers.length; i++) {
    if (i !== numbers.length - 1) {
      newNumbers.push(numbers[i], delimeter);
    } else {
      newNumbers.push(numbers[i]);
    }
  }
  return newNumbers;
};
