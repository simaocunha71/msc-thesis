  let largestNegative = null;
  let smallestPositive = null;
  for  (let i  of lst) {
    if  (i < 0 && (largestNegative === null || i > largestNegative)) {
      largestNegative = i;
    } else if  (i > 0 && (smallestPositive === null || i < smallestPositive)) {
      smallestPositive = i;
    }
  }
  return [largestNegative, smallestPositive];
}



