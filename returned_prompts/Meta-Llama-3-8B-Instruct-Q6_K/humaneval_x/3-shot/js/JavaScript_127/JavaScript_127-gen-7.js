  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  if (end < start) {
    return "NO";
  }

  let length = end - start + 1;

  if (length <= 1) {
    return "NO";
  }

  let isPrime = true;
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      isPrime = false;
      break;
    }
  }

  return isPrime ? "YES" : "NO";
}
// The intersection of the intervals (1, 3), (2, 4) is (2, 3) which its length is 1, which not a prime number.
// So, the function intersection((1, 2), (2, 3)) should return "NO".