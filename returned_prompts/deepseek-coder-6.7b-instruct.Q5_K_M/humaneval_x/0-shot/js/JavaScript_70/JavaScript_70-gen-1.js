  lst.sort((a, b) => a - b);
  let result = [];
  while (lst.length) {
    result.push(lst.shift());
    if (lst.length) {
      result.push(lst.pop());
    }
  }
  return result;
}

strangeSortList([1, 2, 3, 4]); // [1, 4, 2, 3]
strangeSortList([5, 5, 5, 5]); // [5, 5, 5, 5]
strangeSortList([]); // []


*/

function strangeSortList(lst) {
  lst.sort((a, b) => a - b);
  let result = [];
  while (lst.length) {
    result.push(lst.shift());
    if (lst.length) {
      result.push(lst.pop());
    }
  }
  return result;
}

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []

module.exports = strangeSortList;
