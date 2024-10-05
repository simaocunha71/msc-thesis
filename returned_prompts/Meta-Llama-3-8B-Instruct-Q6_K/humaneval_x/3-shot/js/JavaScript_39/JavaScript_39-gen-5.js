  let a = 0, b = 1;
  let count = 0;

  while (true) {
    let temp = a;
    a = b;
    b = temp + b;
    if (isPrime(b) && ++count == n) {
      return b;
    }
  }
}

const isPrime = (n) => {
  if (n < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
}
}  // end of function
}  // end of function


