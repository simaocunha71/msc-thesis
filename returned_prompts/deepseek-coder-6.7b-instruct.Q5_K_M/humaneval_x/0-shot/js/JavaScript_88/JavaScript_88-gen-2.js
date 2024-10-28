  if (array.length === 0) return array;

  let sortedArray = [...array];
  const sum = array[0] + array[array.length - 1];

  return sum % 2 === 0
    ? sortedArray.sort((a, b) => b - a)
    : sortedArray.sort((a, b) => a - b);
};

console.log(sortArray([])); // []
console.log(sortArray([5])); // [5]
console.log(sortArray([2, 4, 3, 0, 1, 5])); // [0, 1, 2, 3, 4, 5]
console.log(sortArray([2, 4, 3, 0, 1, 5, 6])); // [6, 5, 4, 3, 2, 1, 0]

// Tests
console.log(sortArray([1, 2, 3])); // [1, 2, 3]
console.log(sortArray([3, 2, 1])); // [3, 2, 1]
console.log(sortArray([1, 3, 2])); // [3, 2, 1]
console.log(sortArray([2, 1, 3])); // [1, 2, 3]
console.log(sortArray([2, 3, 1])); // [1, 2, 3]
console.log(sortArray([1, 1, 1])); // [1, 1, 1]
console.log(sortArray([1, 2, 2])); // [1, 2, 2]
console.log(sortArray([2, 2, 1])); // [2, 2, 1]
console.log(sortArray([2, 2, 2])); // [2, 2, 2]
console.log(sortArray([2, 1, 1])); // [2, 1, 1]
console.log(sortArray([1, 2, 1])); // [1, 1, 