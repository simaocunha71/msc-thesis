  let min = null;
  let min2 = null;

  for (const num of lst) {
    if (min == null || num < min) {
      min2 = min;
      min = num;
    } else if (min2 == null || num < min2) {
      min2 = num;
    }
  }

  return min2;
}



