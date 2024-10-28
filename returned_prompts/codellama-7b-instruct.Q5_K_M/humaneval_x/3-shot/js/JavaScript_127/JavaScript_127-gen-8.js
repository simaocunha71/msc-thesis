  if (interval1[0] > interval2[1] || interval2[0] > interval1[1]) {
    return "NO";
  }

  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  if (start > end) {
    return "NO";
  }

  let length = end - start;
  if (isPrime(length)) {
    return "YES";
  } else {
    return "NO";
  }
}


