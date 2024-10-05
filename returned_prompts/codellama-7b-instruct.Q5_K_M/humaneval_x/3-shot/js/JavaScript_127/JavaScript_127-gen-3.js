  if (interval1[0] > interval2[1] || interval2[0] > interval1[1]) {
    return "NO";
  }

  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  if (end - start > 1) {
    let result = [];
    for (let i = start; i <= end; i++) {
      if (isPrime(i)) {
        result.push(i);
      }
    }
    return result.length > 0 ? "YES" : "NO";
  }
  return "NO";
}



