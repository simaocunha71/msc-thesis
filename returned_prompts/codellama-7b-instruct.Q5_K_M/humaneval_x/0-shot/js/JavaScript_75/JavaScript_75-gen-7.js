const isPrime = (number) => {
  if (number < 2) {
    return false;
  }
  for (let i = 2; i < number; i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
};

const isMultiply = (a) => {
  if (a < 100) {
    for (let i = 2; i < 10; i++) {
      for (let j = 2; j < 10; j++) {
        if (a === i * j) {
          return true;
        }
      }
    }
  }
  return false;
};

const isMultiplyPrime = (a) => {
  for (let i = 2; i < 10; i++) {
    if (isPrime(i) === false) {
      return false;
    }
    for (let j = 2; j < 10; j++) {
      if (isPrime(j) === false) {
        return false;
      }
      if (a === i * j) {
        return true;
      }
    }
  }
  return false;
};

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(12)); // false
console.log(isMultiplyPrime(90)); // true
console.log(isMultiplyPrime(100)); // false



