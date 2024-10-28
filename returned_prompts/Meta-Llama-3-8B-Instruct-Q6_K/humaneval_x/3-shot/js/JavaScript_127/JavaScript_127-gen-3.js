  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  if (start > end) {
    return "NO";
  }

  let intersection_length = end - start + 1;

  for (let i = 2; i <= Math.sqrt(intersection_length); i++) {
    if (intersection_length % i == 0) {
      return "NO";
    }
  }

  return "YES";
}