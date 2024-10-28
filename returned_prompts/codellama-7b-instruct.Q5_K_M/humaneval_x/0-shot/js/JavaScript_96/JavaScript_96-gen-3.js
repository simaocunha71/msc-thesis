const countUpTo = (n) => {
  const primeNumbers = [];

  for (let i = 2; i < n; i++) {
    if (i % 2 !== 0 && i % 3 !== 0) {
      primeNumbers.push(i);
    }
  }

  return primeNumbers;
};
