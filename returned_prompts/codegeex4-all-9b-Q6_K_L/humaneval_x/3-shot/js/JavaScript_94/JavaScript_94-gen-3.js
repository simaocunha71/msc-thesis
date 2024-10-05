  const isPrime = (num) => {
    if (num <= 1) return false;
    if (num <= 3) return true;

    if (num % 2 === 0 || num % 3 === 0) return false;

    for (let i = 5; i * i <= num; i += 6) {
      if (num % i === 0 || num % (i + 2) === 0) return false;
    }

    return true;
  };

  const largestPrime = (numbers) => {
    let maxPrime = 0;
    for (let num of numbers) {
      if (isPrime(num) && num > maxPrime) {
        maxPrime = num;
      }
    }
    return maxPrime;
  };

  const sumDigits = (number) => {
    let sum = 0;
    while (number > 0) {
      sum += number % 10;
      number = Math.floor(number / 10);
    }
    return sum;
  };

  const largestPrimeNumber = largestPrime(lst);
  return sumDigits(largestPrimeNumber);
}



