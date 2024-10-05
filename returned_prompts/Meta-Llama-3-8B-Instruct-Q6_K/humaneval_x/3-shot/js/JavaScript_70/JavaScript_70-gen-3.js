  if (lst.length === 0) {
    return [];
  }

  let result = [];
  let min = Math.min(...lst);
  let max = Math.max(...lst);

  while (lst.length > 0) {
    result.push(min);
    lst = lst.filter(x => x !== min);
    if (lst.length > 0) {
      min = Math.min(...lst);
      max = Math.max(...lst);
    }
  }
  return result;
}
// test
console.log(strangeSortList([1, 2, 3, 4]));  // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5]));  // [5, 5, 5, 5]
console.log(strangeSortList([]));  // []



