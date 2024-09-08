  const intersectionLength = intersection(interval1, interval2);
  if (intersectionLength < 0) return "NO";
  if (isPrime(intersectionLength)) return "YES";
  return "NO";
}



