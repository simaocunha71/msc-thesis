  const start = Math.max(interval1[0], interval2[0]);
  const end = Math.min(interval1[1], interval2[1]);
  
  if (start > end) {
    return "NO";
  }
  
  const length = end - start + 1;
  
  if (isPrime(length)) {
    return "YES";
  } else {
    return "NO";
  }
}

function isPrime(n) {
  if (n < 2) {
    return false;
  }
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}