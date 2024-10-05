  let maxNeg = null;
  let minPos = null;
  for (const num of lst) {
    if (num < 0 && (maxNeg === null || num > maxNeg)) {
      maxNeg = num;
    } else if (num > 0 && (minPos === null || num < minPos)) {
      minPos = num;
    }
  }
  return [maxNeg, minPos];
}
// OR
const largestSmallestIntegers = (lst) => {
  let maxNeg = null;
  let minPos = null;
  for (const num of lst) {
    if (num < 0) {
      maxNeg = num;
    } else if (num > 0 && (minPos === null || num < minPos)) {
      minPos = num;
    }
  }
  return [maxNeg !== null ? maxNeg : null, minPos !== null ? minPos : null];
}