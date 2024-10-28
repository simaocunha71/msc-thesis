  const sum = q.reduce((a, b) => a + b, 0);
  const isPalindrome = q.toString() === q.reverse().toString();
  return sum <= w && isPalindrome;
};
*/

const willItFly = (q, w) => {
  const sum = q.reduce((a, b) => a + b, 0);
  const isPalindrome = q.toString() === q.reverse().toString();
  return sum <= w && isPalindrome;
};

console.log(willItFly([1, 2], 5)); // false
console.log(willItFly([3, 2, 3], 1)); // false
console.log(willItFly([3, 2, 3], 9)); // true
console.log(willItFly([3], 5)); // true

// output: false, false, true, true

// function willItFly(q, w) {
//   let sum = 0;
//   let reverse = [];
//   for (let i = 0; i < q.length; i++) {
//     sum += q[i];
//     reverse.unshift(q[i]);
//   }
//   return sum <= w && q.join("") === reverse.join("");
// }

// console.log(willItFly([1, 2], 5)); // false
// console.log(willItFly([3, 2, 3], 1)); // false
// console.log(willItFly([3, 2, 3], 9)); // true
// console.log(willItFly([3], 5)); // true
// Output: false, false, true, true

// function willItFly(q, w) {
//   return q.join("") === q.reverse().join("") && q.reduce((a, b) => a + b) <= w;
// }

// console.log(willItFly([1, 2], 5)); // false
// console.log(willItFly([3, 2, 3