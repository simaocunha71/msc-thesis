  const sum = q.reduce((a, b) => a + b, 0);
  const isPalindrome = q.toString() === q.reverse().toString();
  return sum <= w && isPalindrome;
}

console.log(willItFly([1, 2], 5)); // false
console.log(willItFly([3, 2, 3], 1)); // false
console.log(willItFly([3, 2, 3], 9)); // true
console.log(willItFly([3], 5)); // true



*/

const willItFly = (q, w) => {
  const sum = q.reduce((a, b) => a + b, 0);
  const isPalindrome = q.toString() === q.reverse().toString();
  return sum <= w && isPalindrome;
}

console.log(willItFly([1, 2], 5)); // false
console.log(willItFly([3, 2, 3], 1)); // false
console.log(willItFly([3, 2, 3], 9)); // true
console.log(willItFly([3], 5)); // true

// The function willItFly takes as input an array q and a number w. The array q represents the weight of the object, and w is the maximum possible weight that the object can carry. It checks if the sum of the weights is less than or equal to w and if the array q is a palindrome. If both conditions are met, it returns true, otherwise it returns false.
































































































































