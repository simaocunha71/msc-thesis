  let max = -Infinity;
  let result = 0;
  for (const number of lst) {
    if (number > max && isPrime(number)) {
      result = sumDigits(number);
      max = number;
    }
  }
  return result;
};

const isPrime = (number) => {
  if (number % 2 === 0 || number % 3 === 0) return false;
  for (let i = 5; i * i <= number; i += 6) {
    if (number % i === 0 || number % (i + 2) === 0) return false;
  }
  return true;
}

const sumDigits = (number) => {
  let result = 0;
  while (number > 0) {
    result += number % 10;
    number = Math.floor(number / 10);
  }
  return result;
}



