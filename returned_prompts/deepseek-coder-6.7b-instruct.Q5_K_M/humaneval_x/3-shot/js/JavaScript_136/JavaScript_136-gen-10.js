  let largestNegative = null, smallestPositive = null;
  for (let num of lst) {
    if (num > 0 && (smallestPositive === null || num < smallestPositive)) {
      smallestPositive = num;
    } else if (num < 0 && (largestNegative === null || num > largestNegative)) {
      largestNegative = num;
    }
  }
  return [largestNegative, smallestPositive];
}



