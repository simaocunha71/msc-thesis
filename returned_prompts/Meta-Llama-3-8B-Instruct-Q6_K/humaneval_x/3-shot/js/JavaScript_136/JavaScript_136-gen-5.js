  let largestNeg = null;
  let smallestPos = null;
  for (const num of lst) {
    if (num < 0) {
      if (largestNeg === null || num > largestNeg) {
        largestNeg = num;
      }
    } else if (num > 0) {
      if (smallestPos === null || num < smallestPos) {
        smallestPos = num;
      }
    }
  }
  if (largestNeg !== null && smallestPos !== null) {
    return [largestNeg, smallestPos];
  } else {
    return [null, null];
  }
}