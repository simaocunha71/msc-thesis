  let maxNegative = null;
  let minPositive = null;

  for (let i of lst) {
    if (i < 0) {
      if (maxNegative === null || i > maxNegative) {
        maxNegative = i;
      }
    } else if (i > 0) {
      if (minPositive === null || i < minPositive) {
        minPositive = i;
      }
    }
  }

  return [maxNegative, minPositive];
}