  const primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
  ];

  const max_prime = lst.reduce((max_prime, num) => {
    if (primes.includes(num) && num > max_prime) {
      return num;
    } else {
      return max_prime;
    }
  }, 0);

  let digits = 0;

  if (max_prime != 0) {
    digits = max_prime.toString().split('').reduce((digits, num) => {
      return digits + +num;
    }, 0);
  }

  return digits;
}



