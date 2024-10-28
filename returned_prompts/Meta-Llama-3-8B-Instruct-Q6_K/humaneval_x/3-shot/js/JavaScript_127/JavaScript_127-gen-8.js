  let [start1, end1] = interval1;
  let [start2, end2] = interval2;

  if (start1 > end2 || start2 > end1) {
    return "NO";
  }

  let start = Math.max(start1, start2);
  let end = Math.min(end1, end2);

  if (start > end) {
    return "NO";
  }

  let length = end - start + 1;

  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      return "NO";
    }
  }

  return "YES";
}