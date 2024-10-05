  let sum = 0;
  
  for (let i = 0; i < lst.length; i++) {
    if (Number.isInteger(lst[i]) && lst[i] > 0 && lst[i] % 2 !== 0) {
      sum += Math.pow(lst[i], 2);
    }
  }
  
  return sum;
}

console.log(doubleTheDifference([1, 3, 2, 0]));  // 10
console.log(doubleTheDifference([-1, -2, 0]));  // 0
console.log(doubleTheDifference([9, -2]));  // 81
console.log(doubleTheDifference([0]));  // 0
console.log(doubleTheDifference([]));  // 0

*/

/*
TESTS

console.log(doubleTheDifference([1, 3, 2, 0]))  // 10
console.log(doubleTheDifference([-1, -2, 0]))  // 0
console.log(doubleTheDifference([9, -2]))  // 81
console.log(doubleTheDifference([0]))  // 0
console.log(doubleTheDifference([]))  // 0
*/

module.exports = doubleTheDifference;

























































































































































































