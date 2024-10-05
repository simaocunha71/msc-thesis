const largestSmallestIntegers = (lst) => {
  let positive = null;
  let negative = null;
  for (const num of lst) {
    if (num > 0 && (positive === null || num < positive)) {
      positive = num;
    }
    if (num < 0 && (negative === null || num > negative)) {
      negative = num;
    }
  }
  return [negative, positive];
};
