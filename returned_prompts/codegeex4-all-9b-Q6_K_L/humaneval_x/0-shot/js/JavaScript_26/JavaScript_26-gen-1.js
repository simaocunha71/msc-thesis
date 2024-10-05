const removeDuplicates = (numbers) => {
  let uniqueNumbers = [];
  for (let i = 0; i < numbers.length; i++) {
    if (numbers.indexOf(numbers[i]) === i) {
      uniqueNumbers.push(numbers[i]);
    }
  }
  return uniqueNumbers;
};