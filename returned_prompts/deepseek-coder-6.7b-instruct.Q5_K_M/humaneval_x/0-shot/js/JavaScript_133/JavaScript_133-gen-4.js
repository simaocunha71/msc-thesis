  return lst.reduce((total, num) => {
    return total + Math.pow(Math.ceil(num), 2);
  }, 0);
};
console.log(sumSquares([1, 2, 3])); // 14
console.log(sumSquares([1, 4, 9])); // 98
console.log(sumSquares([1, 3, 5, 7])); // 84
console.log(sumSquares([1.4, 4.2, 0])); // 29
console.log(sumSquares([-2.4, 1, 1])); // 6

// This program uses the reduce method of JavaScript to iterate over each element in the input list.
// Math.ceil is used to round each number to the nearest integer (upwards).
// Math.pow is then used to square the rounded number.
// The squared number is added to the running total, which is returned as the final result.
// The process is repeated for each element in the list, resulting in the sum of the squared and rounded numbers.
// The reduce method takes two arguments: an accumulator (total) and the current value (num).
// For each iteration, the current value is rounded, squared, and added to the accumulator.
// The second argument to reduce is the initial value of the accumulator, which is 0 in this case.
// The reduce method returns the final value of the accumulator.
// In this case, the final value is the sum of the squared and rounded numbers in the list.

// The time complexity of this program is O(n), where n is the length of the input list.
// This is because the program iterates over each element in the list once.
// The space complexity is O(1), as the program uses a constant amount of space to store the running total and the current value.
// The running total is updated in-place, so no additional space is needed for this.
// The space complexity of the reduce method used here is also O(1), as it does not create any additional data structures that grow with the input size.
// Therefore, the overall space complexity of the program is O(1).
// The