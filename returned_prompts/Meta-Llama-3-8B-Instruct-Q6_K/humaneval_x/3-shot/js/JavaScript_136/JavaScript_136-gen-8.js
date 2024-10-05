  let largestNegative = null;
  let smallestPositive = null;

  for (const num of lst) {
    if (num < 0) {
      largestNegative = largestNegative === null ? num : Math.max(largestNegative, num);
    } else if (num > 0) {
      smallestPositive = smallestPositive === null ? num : Math.min(smallestPositive, num);
    }
  }

  return [largestNegative, smallestPositive];
}