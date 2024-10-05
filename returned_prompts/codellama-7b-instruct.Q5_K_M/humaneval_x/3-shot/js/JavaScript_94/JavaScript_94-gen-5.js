  let result = 0;

  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      result += getSumOfDigits(lst[i]);
    }
  }

  return result;
}



