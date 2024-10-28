  let maxNeg = null;
  let minPos = null;

  for (let num of lst) {
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

  return [maxNeg === null ? null : maxNeg, minPos === null ? null : minPos];
}