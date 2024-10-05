  if (interval1[1] < interval2[0] || interval1[0] > interval2[1]) {
    return "NO";
  }

  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  return (end - start) % 2 == 0 ? "NO" : "YES";
}



