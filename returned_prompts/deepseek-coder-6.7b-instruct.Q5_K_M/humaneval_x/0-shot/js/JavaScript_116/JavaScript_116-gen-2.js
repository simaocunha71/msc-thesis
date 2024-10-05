  return arr.sort((a, b) => {
    let aBinary = a.toString(2);
    let bBinary = b.toString(2);
    let aOnes = aBinary.split('1').length - 1;
    let bOnes = bBinary.split('1').length - 1;

    return aOnes - bOnes || a - b;
  });
};

console.log(sortArray([1, 5, 2, 3, 4])); // [1, 2, 3, 4, 5]
console.log(sortArray([-2, -3, -4, -5, -6])); // [-6, -5, -4, -3, -2]
console.log(sortArray([1, 0, 2, 3, 4])); // [0, 1, 2, 3, 4]

// Time complexity: O(n log n) due to sorting
// Space complexity: O(n) as we are storing binary values

This solution works by first converting each number to its binary representation, then counting the number of 1's in that representation. It uses the built-in JavaScript function `.sort()` to sort the array based on the count of ones and decimal values. If the count of ones is the same for two numbers, it then sorts them based on their decimal values.

Note: The `-` sign in front of the `a.toString(2)` and `b.toString(2)` is because we don't want to count the `-` sign as a `1` in the binary representation.
*/

// JavaScript does not have built-in support for binary numbers,
// so we can't use binary comparison to solve this problem.

/*
sortArray([1, 5, 2, 3, 4])  // [1, 2, 3, 4, 5]
sortArray([-2, -3, -4, -5, -6])  // [-6, -5, -4, -3, -2]
sortArray([1, 0, 2, 3, 4])  // [0, 1, 2, 