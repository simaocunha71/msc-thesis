  if (lst.length === 0) {
    return [];
  }

  lst.sort((a, b) => a - b);
  let result = [lst[0]];
  for (let i = 1; i < lst.length; i++) {
    let min = Infinity, max = -Infinity;
    for (let j = 0; j < lst.length; j++) {
      if (j !== i && (lst[j] < min || lst[j] > max)) {
        if (lst[j] < min) {
          min = lst[j];
        } else if (lst[j] > max) {
          max = lst[j];
        }
      }
    }
    result.push(max);
    lst[lst.indexOf(max)] = min;
  }
  return result;
}
// test cases
console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []



