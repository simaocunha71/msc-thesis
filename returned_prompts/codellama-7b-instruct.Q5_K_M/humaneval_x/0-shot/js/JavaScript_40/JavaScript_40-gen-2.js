/*
  triplesSumToZero takes a list of integers as an input.
  it returns true if there are three distinct elements in the list that
  sum to zero, and false otherwise.

  >>> triplesSumToZero([1, 3, 5, 0])
  false
  >>> triplesSumToZero([1, 3, -2, 1])
  true
  >>> triplesSumToZero([1, 2, 3, 7])
  false
  >>> triplesSumToZero([2, 4, -5, 3, 9, 7])
  true
  >>> triplesSumToZero([1])
  false
  */
const triplesSumToZero = (l) => {

  // 1. check if the list is long enough to contain three distinct elements
  //    that sum to zero
  if (l.length < 3) {
    return false;
  }

  // 2. sort the list
  const sorted = l.sort((a, b) => a - b);

  // 3. check if the first, second, and last elements sum to zero
  if (sorted[0] + sorted[1] + sorted[sorted.length - 1] === 0) {
    return true;
  }

  // 4. otherwise, return false
  return false;
};
