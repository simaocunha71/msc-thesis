  let sum = array[0] + array[array.length - 1];
  if (sum % 2 === 0) {
    array.sort((a, b) => b - a);
  } else {
    array.sort((a, b) => a - b);
  }
  return array.slice();
}
// Test cases
console.log(sortArray([])); // []
console.log(sortArray([5])); // [5]
console.log(sortArray([2, 4, 3, 0, 1, 5])); // [0, 1, 2, 3, 4, 5]
console.log(sortArray([2, 4, 3, 0, 1, 5, 6])); // [6, 5, 4, 3, 2, 1, 0]