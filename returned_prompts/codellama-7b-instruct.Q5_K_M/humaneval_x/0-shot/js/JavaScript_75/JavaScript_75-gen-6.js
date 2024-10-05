  //Write your code here
  const primeNumbers = [2, 3, 5];
  let primeNumbersCounter = 0;
  for (let i = 0; i < primeNumbers.length; i++) {
    for (let j = 0; j < a; j++) {
      if (primeNumbers[i] === j) {
        primeNumbersCounter++;
      }
    }
  }
  if (primeNumbersCounter === 3) {
    return true;
  } else {
    return false;
  }
}

function testIsMultiplyPrime() {
  assert.equal(isMultiplyPrime(30), true, "30 is a product of 2, 3 and 5");
  assert.equal(isMultiplyPrime(35), false, "35 is not a product of 3 prime numbers");
}

module.exports = {
  isMultiplyPrime,
  testIsMultiplyPrime,
};
