const largestDivisor = (n) => {
  // return n % 2 === 0 ? n / 2 : n;
  return n % 2 === 0 ? n / 2 : largestDivisor(n / 2);
};

