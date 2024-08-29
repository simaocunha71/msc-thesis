  if (interval1[1] < interval2[0] || interval2[1] < interval1[0]) {
    return "NO";
  }

  const start = Math.max(interval1[0], interval2[0]);
  const end = Math.min(interval1[1], interval2[1]);
  const length = end - start + 1;

  if (length <= 1) {
    return "NO";
  }

  let isPrime = true;
  for (let i = 2; i < length; i++) {
    if (length % i === 0) {
      isPrime = false;
      break;
    }
  }

  return isPrime ? "YES" : "NO";
};



