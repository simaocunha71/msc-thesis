  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  if (start <= end) {
    return end - start + 1;
  } else {
    return 0;
  }
}



