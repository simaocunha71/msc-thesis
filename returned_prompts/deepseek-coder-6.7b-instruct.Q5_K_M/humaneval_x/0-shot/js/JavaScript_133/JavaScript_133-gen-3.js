  let sum = 0;
  for(let i = 0; i < lst.length; i++) {
    sum += Math.pow(Math.ceil(lst[i]), 2);
  }
  return sum;
};

console.log(sumSquares([1,2,3])); // 14
console.log(sumSquares([1,4,9])); // 98
console.log(sumSquares([1,3,5,7])); // 84
console.log(sumSquares([1.4,4.2,0])); // 29
console.log(sumSquares([-2.4,1,1])); // 6

*/

const sumSquares = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    sum += Math.pow(Math.ceil(lst[i]), 2);
  }
  return sum;
};

console.log(sumSquares([1, 2, 3])); // 14
console.log(sumSquares([1, 4, 9])); // 98
console.log(sumSquares([1, 3, 5, 7])); // 84
console.log(sumSquares([1.4, 4.2, 0])); // 29
console.log(sumSquares([-2.4, 1, 1])); // 6

// 98, 84, 29, 6

// 