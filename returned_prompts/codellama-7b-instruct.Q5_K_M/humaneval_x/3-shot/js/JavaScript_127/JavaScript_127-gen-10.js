  if (interval1[1] < interval2[0] || interval2[1] < interval1[0]) {
    return "NO";
  }

  const start = Math.max(interval1[0], interval2[0]);
  const end = Math.min(interval1[1], interval2[1]);

  if (start > end) {
    return "NO";
  }

  const length = end - start + 1;

  if (isPrime(length)) {
    return "YES";
  }

  return "NO";
}



