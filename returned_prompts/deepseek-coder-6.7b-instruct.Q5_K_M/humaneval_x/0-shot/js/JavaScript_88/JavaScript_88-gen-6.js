  let newArray = array.slice();
  let sum = array[0] + array[array.length - 1];

  if (sum % 2 === 0) {
    newArray.sort((a, b) => b - a);
  } else {
    newArray.sort((a, b) => a - b);
  }

  return newArray;
};

console.log(sortArray([])); // []
console.log(sortArray([5])); // [5]
console.log(sortArray([2, 4, 3, 0, 1, 5])); // [0, 1, 2, 3, 4, 5]
console.log(sortArray([2, 4, 3, 0, 1, 5, 6])); // [6, 5, 4, 3, 2, 1, 0]

// This code will take in an array, create a copy of the array, and then sort it based on the sum of the first and last elements. If the sum is even, it will sort it in descending order; if the sum is odd, it will sort it in ascending order. Finally, it returns the sorted array.

// The sort method is used with a callback function that determines the sort order based on the difference between a and b. If the result is less than 0, a is sorted to an index lower than b. If the result is 0, a and b remain unchanged with respect to each other. If the result is greater than 0, b is sorted to an index lower than a.

// The % operator is used to find the remainder of the sum divided by 2, which tells us if the sum is odd or even.

// The sort method changes the original array, so we need to create a copy of the array first.

// The time complexity of this solution is O(n log n), where n is the length of the array. This is due to the sort operation, which takes O(n log n) time in the average and worst-case scenarios.

// The space complexity is O(n), as we are creating a copy of the array.

// This solution assumes that the array will always contain at least one element. If the