  let largestNegative = null;
  let smallestPositive = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (largestNegative === null || lst[i] > largestNegative)) {
      largestNegative = lst[i];
    } else if (lst[i] > 0 && (smallestPositive === null || lst[i] < smallestPositive)) {
      smallestPositive = lst[i];
    }
  }

  return [largestNegative, smallestPositive];
}



