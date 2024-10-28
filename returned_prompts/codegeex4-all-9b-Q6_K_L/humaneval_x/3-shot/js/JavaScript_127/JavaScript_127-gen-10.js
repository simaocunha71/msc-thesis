  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);
  let len = end - start + 1;

  if (len <= 1) {
    return "NO";
  }

  for (let i = 2; i <= Math.sqrt(len); i++) {
    if (len % i == 0) {
      return "NO";
    }
  }

  return "YES";
}