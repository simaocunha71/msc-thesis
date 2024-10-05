/*
  The solution is to find the number of times the two sets of cars will meet at the
  same point.  This occurs when the distance between two cars in the left to right
  set is equal to the distance between two cars in the right to left set.
  */

  const distance = n * 2;
  const meetCount = distance / 2;

  return meetCount * (meetCount - 1) / 2;
}
