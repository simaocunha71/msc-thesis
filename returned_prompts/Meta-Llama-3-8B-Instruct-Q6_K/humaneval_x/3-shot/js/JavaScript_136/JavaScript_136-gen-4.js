  let largestNegative = null;
  let smallestPositive = null;
  for (let num of lst) {
    if (num < 0) {
      if (largestNegative === null || num > largestNegative) {
        largestNegative = num;
      }
    } else if (num > 0) {
      if (smallestPositive === null || num < smallestPositive) {
        smallestPositive = num;
      }
    }
  }
  return [largestNegative, smallestPositive];
}