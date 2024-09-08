  const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i <= Math.sqrt(n); i += 1) {
      if (n % i === 0) return false;
    }
    return true;
  };

  const sumDigits = (n) => {
    if (n < 0) return -1;
    if (n === 0) return 0;
    return Number(String(n).split('').reduce((a, b) => a + +b, 0));
  };

  const maxPrime = (lst) => {
    return lst.filter(isPrime).sort((a, b) => b - a).pop();
  };

  const maxSum = (lst) => {
    return lst.map(maxPrime).map(sumDigits).reduce((a, b) => a + b, 0);
  };

  return maxSum(lst);
};



