  // Sorting the array in descending order
  arr.sort((a, b) => b - a);
  
  // Returning the first k elements
  return arr.slice(0, k);
};

console.log(maximum([-3, -4, 5], 3)); // [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // [2]

This problem is a variation of the typical "k-largest numbers" problem. We just need to sort the array in descending order and then return the first k elements. This solution has a time complexity of O(n log n) due to the sorting operation.
*/

// The JavaScript solution
function maximum(arr, k) {
  // Sorting the array in descending order
  arr.sort((a, b) => b - a);

  // Returning the first k elements
  return arr.slice(0, k);
}

console.log(maximum([-3, -4, 5], 3)); // [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // [2]

/*
  Explanation:

  In the first example, the maximum 3 numbers are -4, -3, and 5.

  In the second example, the maximum 2 numbers are 4 and 4.

  In the third example, the maximum number is 2.
 */

// The Python solution
def maximum(arr, k):
  # Sorting the array in descending order
  arr.sort(reverse=True)

  # Returning the first k elements
  return arr[:k]

print(maximum([-3, -4, 5], 3)) # [-4, -3, 5]
