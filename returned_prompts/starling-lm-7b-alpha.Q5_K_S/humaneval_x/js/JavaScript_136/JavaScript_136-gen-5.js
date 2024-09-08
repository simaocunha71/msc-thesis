  let negative = null, positive = null;
  for (const n of lst) {
    if (n < 0) {
      if (negative === null || negative < n) {
        negative = n;
      }
    } else if (n > 0) {
      if (positive === null || positive > n) {
        positive = n;
      }
    }
  }
  return [negative, positive];
}



