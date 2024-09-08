  const stringLength = string.length;

  function isPrime(num) {
    if (num === 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  }

  if (isPrime(stringLength)) {
    return true;
  } else {
    return false;
  }
}



