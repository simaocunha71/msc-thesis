  const start1 = interval1[0];
  const end1 = interval1[1];
  const start2 = interval2[0];
  const end2 = interval2[1];

  if (start1 <= end2 && start2 <= end1) {
    const start = Math.max(start1, start2);
    const end = Math.min(end1, end2);
    const result = end - start;
    if (result > 1) {
      if (isPrime(result)) {
        return "YES";
      } else {
        return "NO";
      }
    } else {
      return "NO";
    }
  } else {
    return "NO";
  }
}



