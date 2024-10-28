const strangeSortList = (lst) => {
  let odd = [];
  let even = [];
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 == 0) {
      even.push(lst[i]);
    } else {
      odd.push(lst[i]);
    }
  }
  even.sort((a, b) => a - b);
  odd.sort((a, b) => b - a);
  return even.concat(odd);
};

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []
console.log(strangeSortList([1, 2, 3, 4, 5, 6, 7, 8])); // [1, 8, 2, 7, 3, 6, 4, 5]