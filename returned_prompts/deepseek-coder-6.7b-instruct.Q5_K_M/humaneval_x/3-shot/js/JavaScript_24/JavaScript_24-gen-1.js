  for  (let i = n - 1; i > 0; i--) {
    if  (n % i == 0) {
      return i;
    }
  }
  return -1; // if no divisor found, return -1
}



