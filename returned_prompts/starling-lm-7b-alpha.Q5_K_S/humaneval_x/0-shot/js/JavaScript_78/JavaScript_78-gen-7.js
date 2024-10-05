
  const hexMap = {
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

  const primes = [2, 3, 5, 7, 11, 13, 17];

  let count = 0;

  for (let i = 0; i < num.length; i++) {
    const currentHex = num[i];
    if (primes.includes(hexMap[currentHex])) {
      count += 1;
    }
  }

  return count;
};

hexKey('ABED1A33');

























































































































































































































































