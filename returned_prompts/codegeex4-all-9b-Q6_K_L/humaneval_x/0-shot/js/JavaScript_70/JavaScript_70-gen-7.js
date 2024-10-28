const strangeSortList = (lst) => {
  let arr = [...lst];
  let result = [];
  while (arr.length) {
    result.push(Math.min(...arr));
    arr.splice(arr.indexOf(Math.min(...arr)), 1);
    if (arr.length) {
      result.push(Math.max(...arr));
      arr.splice(arr.indexOf(Math.max(...arr)), 1);
    }
  }
  return result;
};