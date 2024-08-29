  let hex_key = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
  };
  return hex_key[num];
}
const hexPrimes = [2, 3, 5, 7, 11, 13, 17];

const hexPrimeCounter = (num) => {
  let result = 0;
  const num_array = num.split('');
  for (const digit of num_array) {
    if (hexKey(digit) in hexPrimes) {
      result += 1;
    }
  }
  return result;
};



