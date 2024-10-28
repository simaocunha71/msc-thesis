  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);
  let len = end - start;

  if (len < 0) {
    return "NO";
  }

  for (let i = 2; i < Math.sqrt(len) + 1; i++) {
    if (len % i == 0) {
      return "NO";
    }
  }

  return "YES";
}