  const isPrime = (num) => {
    for (let i = 2; i < num; i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  };

  const sumDigits = (num) => {
    let sum = 0;
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    return sum;
  };

  let max = 0;
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      max = lst[i];
    }
  }
  return sumDigits(max);
};



