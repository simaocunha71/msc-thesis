  return arr.sort((a, b) => {
    let count1 = (a.toString(2)).split('1').length - 1;
    let count2 = (b.toString(2)).split('1').length - 1;
    if (count1 === count2) {
      return a - b;
    }
    return count1 - count2;
  });
}
// test cases
console.log(sortArray([1, 5, 2, 3, 4])); // [1, 2, 3, 4, 5]
console.log(sortArray([-2, -3, -4, -5, -6])); // [-6, -5, -4, -3, -2]
console.log(sortArray([1, 0, 2, 3, 4])); // [0, 1, 2, 3, 4]
console.log(sortArray([5, 6, 7, 8, 9])); // [5, 6, 7, 8, 9]
console.log(sortArray([1, 1, 1, 1])); // [1, 1, 1, 1]
console.log(sortArray([2, 2, 2, 2])); // [2, 2, 2, 2]
console.log(sortArray([3, 3, 3, 3])); // [3, 3, 3, 3]
console.log(sortArray([4, 4, 4, 4])); // [4, 4, 4, 4]
console.log(sortArray([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(sortArray([6, 6, 6, 6])); // [6, 6, 6, 6]
console.log(sortArray([7, 7, 7, 7])); // [7, 7, 7, 7]
console.log(sortArray([8, 8, 8, 8])); // [8, 8, 8, 8]
console.log(sortArray([9, 9, 9, 9])); // [9, 9, 9, 9]
console.log(sortArray([-1, -2, -3, -4, -5])); // [-5, -4, -