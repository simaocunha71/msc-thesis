  let max = -Infinity;
  return numbers.map(num => {
    max = Math.max(max, num);
    return max;
  });
}

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]

*/

const rollingMax = (numbers) => {
  let max = -Infinity;
  return numbers.map(num => {
    max = Math.max(max, num);
    return max;
  });
}

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]

// This solution works by using the JavaScript map method to iterate through the array of numbers. 
// For each number, it updates the max variable to be the maximum of the current number and the previous max. 
// This effectively keeps track of the maximum value seen so far in the list.
// The map function returns a new array, so the result of the rollingMax function is a list of the maximum values up to that point in the input list.

// The time complexity of this solution is O(n), where n is the length of the input list. This is because it needs to iterate through the list once to compute the result.
// The space complexity is also O(n), as the function needs to create a new list to store the result.

// The rollingMax function uses the built-in JavaScript Math.max function to find the maximum of the current number and the current max, and the built-in JavaScript Array.map function to apply this operation to each number in the list.

// The rollingMax function does not mutate the input list, as the map function creates a new array without modifying the original list.

// The rollingMax function handles negative numbers correctly.

// The rollingMax function handles the case where the input list is empty correctly, returning an empty list.

// The rollingMax function handles the case where the input list contains only one number correctly, returning a list with a single element equal to that