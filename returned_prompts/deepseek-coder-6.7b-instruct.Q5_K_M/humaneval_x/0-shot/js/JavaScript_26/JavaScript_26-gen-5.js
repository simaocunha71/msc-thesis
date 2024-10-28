  let seen = {};
  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    if (!seen[numbers[i]]) {
      seen[numbers[i]] = true;
      result.push(numbers[i]);
    }
  }

  return result;
};

console.log(removeDuplicates([1, 2, 3, 2, 4])); // [1, 3, 4]

// Explanation:
// Create a seen object to keep track of the numbers that have been seen.
// Iterate through the numbers array, if a number has not been seen before,
// add it to the result array and mark it as seen in the seen object.
// Finally return the result array which will contain the numbers in the order they appeared in the input array but with all duplicates removed.


This solution has a time complexity of O(n) and a space complexity of O(n) as it needs to store a seen object and the result array.
*/

// Solution 2
/*
