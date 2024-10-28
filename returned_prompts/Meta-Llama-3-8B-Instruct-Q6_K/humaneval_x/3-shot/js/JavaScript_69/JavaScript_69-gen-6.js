  let maxCount = 0;
  let maxNum = -1;

  for (let num of lst) {
    let count = lst.filter(x => x === num).length;
    if (count >= num && count > maxCount) {
      maxCount = count;
      maxNum = num;
    }
  }

  return maxNum > 0 ? maxNum : -1;
}
// Test cases
console.log(search([4, 1, 2, 2, 3, 1])) // 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) // 3
console.log(search([5, 5, 4, 4, 4])) // -1
console.log(search([2, 2, 2, 2])) // 2
console.log(search([1, 1, 1, 1])) // 1
console.log(search([1])) // 1
console.log(search([3])) // 3
console.log(search([10, 10, 10, 10])) // 10
console.log(search([1, 2, 3, 4, 5])) // -1
console.log(search([6])) // 6
console.log(search([1, 1, 1, 1, 1])) // 1
console.log(search([1, 2, 3, 4, 5, 6])) // -1
console.log(search([1, 2, 2, 2, 2, 3, 3, 3, 3, 3])) // 3
console.log(search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) // 1
console.log(search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])) // 2
console.log(search([1, 2, 2, 2, 2, 3, 3, 3, 3, 3])) // 3
console.log(search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) // 1
