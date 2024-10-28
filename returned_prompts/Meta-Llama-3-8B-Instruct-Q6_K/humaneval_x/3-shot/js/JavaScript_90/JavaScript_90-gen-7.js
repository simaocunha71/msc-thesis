  if (lst.length < 2) {
    return null;
  }
  let smallest = Infinity;
  let secondSmallest = null;
  for (let num of lst) {
    if (num < smallest) {
      secondSmallest = smallest;
      smallest = num;
    } else if (num < secondSmallest && num !== smallest) {
      secondSmallest = num;
    }
  }
  return secondSmallest === null ? null : secondSmallest;
}