  return {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
  }
}

const hexPrimes = [2, 3, 5, 7, 11, 13, 17];

const isPrime = (num) => {
  if (num === 2 || num === 3 || num === 5 || num === 7 || num === 11 || num === 13 || num === 17) {
    return true;
  }
  if (num % 2 === 0 || num % 3 === 0 || num % 5 === 0 || num % 7 === 0 || num % 11 === 0 || num % 13 === 0 || num % 17 === 0) {
    return false;
  }
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

const hexadecimalPrimes = (str) => {
  let result = 0;
  for (const char of str) {
    if (isPrime(hexKey[char])) {
      result++;
    }
  }
  return result;
}



