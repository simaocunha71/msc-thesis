  let primeNumbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
  let length = string.length;
  for (let i = 0; i < primeNumbers.length; i++) {
    if (primeNumbers[i] == length) {
      return true;
    }
  }
  return false;
}



