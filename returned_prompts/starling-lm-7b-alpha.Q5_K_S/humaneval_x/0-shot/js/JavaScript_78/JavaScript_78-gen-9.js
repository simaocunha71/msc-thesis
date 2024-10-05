  const hexKey = {
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
  };

  let number = 0;
  let result = 0;

  for (let i = 0; i < num.length; i++) {
    number = hexKey[num[i]];
    if (prime(number)) {
      result++;
    }
  }

  return result;
};

function prime(num) {
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num > 1;
}

console.log(hexKey("ABED1A33"));

















































































































































































































