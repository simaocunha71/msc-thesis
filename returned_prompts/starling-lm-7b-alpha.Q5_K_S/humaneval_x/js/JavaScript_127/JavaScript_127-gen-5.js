  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);
  let length = end - start + 1;

  if (length <= 0) {
    return "NO";
  }

  for (let i = 2; i <= length; i++) {
    if (length % i == 0) {
      return "NO";
    }
  }

  return "YES";
}


