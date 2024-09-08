  let min = null;
  let max = null;
  let foundNeg = false;
  let foundPos = false;

  for (const n of lst) {
    if (n < 0) {
      if (foundPos) {
        max = n;
      } else {
        max = Math.max(n, max);
        foundNeg = true;
      }
    } else if (n > 0) {
      if (foundNeg) {
        min = n;
      } else {
        min = Math.min(n, min);
        foundPos = true;
      }
    }
  }

  if (foundNeg && foundPos) {
    return [max, min];
  } else {
    return [min, max];
  }
}



