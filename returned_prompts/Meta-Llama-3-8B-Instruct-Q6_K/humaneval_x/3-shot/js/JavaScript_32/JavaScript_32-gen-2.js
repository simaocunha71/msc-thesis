  if (xs.length % 2 === 0) {
    let x = -xs[1] / xs[0];
    return x;
  } else {
    return null;
  }
}
// test cases
console.log(hasCloseElements([1.0, 2.0, 3.0], 0.5)); // false
console.log(hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)); // true

console.log(separateParenGroups('( ) (( )) (( )( ))')); // ['()', '(())', '(()())']

console.log(truncateNumber(3.5)); // 0.5

console.log(poly([1, 2], 1)); // 3

console.log(round(findZero([1, 2]), 2)); // -0.5
console.log(round(findZero([-6, 11, -6, 1]), 2)); // 1.0
console.log(findZero([1, 2, 3])); // null
console.log(findZero([-6, 11])); // null
console.log(findZero([1])); // null
console.log(findZero([1, 2, 3, 4, 5])); // null
console.log(findZero([-1, 0, 1, 0])); // 0
console.log(findZero([-1, 0, 1])); // null
console.log(findZero([-1, 0, 1, 2])); // null
console.log(findZero([-1, 0, 1, 2, 3])); // null
console.log(findZero([-1, 0, 1, 2, 3, 4])); // null
console.log(findZero([-1, 0, 1, 2, 3, 4, 5])); // null
console.log(findZero([-1, 0, 1, 2, 3, 4, 5, 6])); // null
console.log(findZero([-1, 0, 1, 2, 3, 4, 5, 6, 7])); // null
console.log(findZero([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8])); // null
