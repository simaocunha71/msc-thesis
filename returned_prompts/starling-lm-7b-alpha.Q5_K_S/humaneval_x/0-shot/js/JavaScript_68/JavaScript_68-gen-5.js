
// Pluck one of the nodes and return it.

// The plucked node should be the node with the smallest even value.

// If multiple nodes with the same smallest even value are found return the node that has smallest index.

// The plucked node should be returned in a list, [ smallest_value, its index ],

// If there are no even values or the given array is empty, return [].

// Example 1:

// Input: [4,2,3]

// Output: [2, 1]

// Explanation: 2 has the smallest even value, and 2 has the smallest index.

// Example 2:

// Input: [1,2,3]

// Output: [2, 1]

// Explanation: 2 has the smallest even value, and 2 has the smallest index.

// Example 3:

// Input: []

// Output: []

// Example 4:

// Input: [5, 0, 3, 0, 4, 2]

// Output: [0, 1]

// Explanation: 0 is the smallest value, but  there are two zeros,

//               so we will choose the first zero, which has the smallest index.

// Constraints:

// * 1 <= nodes.length <= 10000

// * 0 <= node.value

  let result = [];

  for(let i = 0; i < arr.length; i++) {
    if(arr[i] % 2 === 0 && result.length === 0) {
      result = [arr[i], i];
    } else if(arr[i] % 2 === 0 && arr[i] < result[0]) {
      result = [arr[i], i];
    } else if(arr[i] % 2 === 0 && arr[i] === result[0] && i < result[1]) {
      result = [arr[i], i];
    }
  }

  return result;
};






















