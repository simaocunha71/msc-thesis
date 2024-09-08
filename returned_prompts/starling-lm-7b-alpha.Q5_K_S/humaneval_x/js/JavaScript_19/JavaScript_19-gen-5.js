  const sortedNumbers = [];
  const numbersArray = numbers.split(' ');
  for (const number of ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']) {
    for (const n of numbersArray) {
      if (n === number) {
        sortedNumbers.push(n);
        numbersArray.splice(numbersArray.indexOf(n), 1);
      }
    }
  }

  return sortedNumbers.join(' ');
}



