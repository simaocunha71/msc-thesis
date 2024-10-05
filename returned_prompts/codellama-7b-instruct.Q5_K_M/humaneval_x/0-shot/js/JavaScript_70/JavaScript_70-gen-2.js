const strangeSortList = (lst) => {
  const result = [];
  const min = Math.min(...lst);
  const max = Math.max(...lst);
  if (min === max) {
    return [min];
  }
  for (let i = 0; i < lst.length; i += 1) {
    if (lst[i] === min) {
      result.push(min);
      result.push(max);
      break;
    }
    if (lst[i] === max) {
      result.push(min);
      result.push(max);
      break;
    }
  }
  return result;
};
