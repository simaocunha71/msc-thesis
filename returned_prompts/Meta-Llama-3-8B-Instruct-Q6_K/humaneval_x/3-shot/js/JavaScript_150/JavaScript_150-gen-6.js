  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
}

// Helper function to check if a number is prime
function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}
}