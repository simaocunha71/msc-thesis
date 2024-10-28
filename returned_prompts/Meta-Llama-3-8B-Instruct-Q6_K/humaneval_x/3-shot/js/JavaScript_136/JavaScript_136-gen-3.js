  let maxNeg = null;
  let minPos = null;

  for (const num of lst) {
    if (num < 0) {
      if (maxNeg === null || num > maxNeg) {
        maxNeg = num;
      }
    } else if (num > 0) {
      if (minPos === null || num < minPos) {
        minPos = num;
      }
    }
  }

  if (maxNeg === null) {
    maxNeg = null;
  }
  if (minPos === null) {
    minPos = null;
  }

  return [maxNeg, minPos];
}