  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
}

// helper function to check if a number is prime
const isPrime = (num) => {
  if (num <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}
}