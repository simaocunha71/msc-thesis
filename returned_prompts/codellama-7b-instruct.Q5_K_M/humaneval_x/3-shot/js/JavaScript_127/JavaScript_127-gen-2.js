  if (interval1[0] > interval1[1] || interval2[0] > interval2[1]) {
    return "NO";
  }

  var start = Math.max(interval1[0], interval2[0]);
  var end = Math.min(interval1[1], interval2[1]);

  if (start > end) {
    return "NO";
  }

  var length = end - start + 1;
  if (isPrime(length)) {
    return "YES";
  } else {
    return "NO";
  }
}



