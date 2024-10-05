  let maxNegative = null;
  let minPositive = null;

  for (const num of lst) {
    if (num < 0) {
      if (maxNegative === null || num > maxNegative) {
        maxNegative = num;
      }
    } else if (num > 0) {
      if (minPositive === null || num < minPositive) {
        minPositive = num;
      }
    }
  }

  return [maxNegative, minPositive];
}



