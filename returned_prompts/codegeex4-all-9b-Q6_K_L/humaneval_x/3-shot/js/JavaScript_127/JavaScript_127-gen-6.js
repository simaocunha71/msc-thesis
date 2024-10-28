  const intersect = (start1, end1, start2, end2) => {
    if (start1 > end1 || start2 > end2) {
      return false;
    }
    const start = Math.max(start1, start2);
    const end = Math.min(end1, end2);
    return end - start >= 0;
  };

  const isPrime = (n) => {
    if (n < 2) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  };

  const start1 = interval1[0];
  const end1 = interval1[1];
  const start2 = interval2[0];
  const end2 = interval2[1];

  if (!intersect(start1, end1, start2, end2)) {
    return "NO";
  }

  const length = Math.min(end1, end2) - Math.max(start1, start2) + 1;
  return isPrime(length) ? "YES" : "NO";
}