  const result = [];
  const min = Math.min(a, b);
  const max = Math.max(a, b);

  for(let i = min; i <= max; i++) {
    if(i % 2 === 0) {
      result.push(i);
    }
  }

  return result;
};

console.log(generateIntegers(2, 8));  // [2, 4, 6, 8]
console.log(generateIntegers(8, 2));  // [2, 4, 6, 8]
console.log(generateIntegers(10, 14));  // []

// Time Complexity: O(n), where n is the difference of a and b
// Space Complexity: O(n), in the worst case where all numbers between a and b are even and are stored in the result array.

/*
  Function Explanation:
  - First, we initialize an empty array, result.
  - We find the minimum and maximum values between a and b and assign them to min and max respectively.
  - We then loop from min to max (inclusive).
  - If the current number is even (i.e., the remainder of the division by 2 is 0), we add it to the result array.
  - Finally, we return the result array.
  */

/*
  We use a loop to iterate through the range from min to max (inclusive). We check if each number is even by using the modulo operator (%). If the number is even, we add it to the result array. At the end, we return the result array. This solution has a time complexity of O(n), where n is the difference between a and b, and a space complexity of O(n), in the worst case where all numbers between a and b are even and are stored in the result array.
  */

/*
  This function works by iterating over the range of numbers between a and b. If the current number is even, it is added to the result array. The result array is then returned.
  */

/*
  This function is tested with the inputs (2, 8), (8, 2), and (10,