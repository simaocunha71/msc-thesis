  let start1 = interval1[0];
  let end1 = interval1[1];
  let start2 = interval2[0];
  let end2 = interval2[1];

  if (end1 < start2 || end2 < start1) {
    return "NO";
  }

  let start = Math.max(start1, start2);
  let end = Math.min(end1, end2);

  return isPrime(end - start + 1) ? "YES" : "NO";
}



