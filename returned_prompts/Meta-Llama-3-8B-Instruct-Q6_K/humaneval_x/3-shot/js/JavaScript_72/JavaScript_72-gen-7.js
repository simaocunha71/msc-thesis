  let sum = q.reduce((a, b) => a + b, 0);
  let isBalanced = JSON.stringify(q) === JSON.stringify(q).split('').reverse().join('');
  return isBalanced && sum <= w;
}
// test cases
console.log(willItFly([1, 2], 5)); // false
console.log(willItFly([3, 2, 3], 1)); // false
console.log(willItFly([3, 2, 3], 9)); // true
console.log(willItFly([3], 5)); // true
// end of test cases
// test case
console.log(willItFly([1, 2, 3, 2, 1], 10)); // true
// end of test case
// end of test cases
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of test case
// end of