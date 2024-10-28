  var result = 0;

  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      result += sumDigits(lst[i]);
    }
  }

  return result;
}



