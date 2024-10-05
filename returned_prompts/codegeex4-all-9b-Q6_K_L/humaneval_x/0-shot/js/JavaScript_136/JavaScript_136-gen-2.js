const largestSmallestIntegers = (lst) => {
  let negative = null;
  let positive = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (negative === null || lst[i] > negative)) {
      negative = lst[i];
    } else if (lst[i] > 0 && (positive === null || lst[i] < positive)) {
      positive = lst[i];
    }
  }
  return [negative, positive];
};