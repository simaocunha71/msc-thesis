  let largestNegative = null;
  let smallestPositive = null;

  for (let num of lst) {
    if (num < 0 && (largestNegative === null || num > largestNegative)) {
      largestNegative = num;
    } else if (num > 0 && (smallestPositive === null || num < smallestPositive)) {
      smallestPositive = num;
    }
  }

  return [largestNegative, smallestPositive];
}



