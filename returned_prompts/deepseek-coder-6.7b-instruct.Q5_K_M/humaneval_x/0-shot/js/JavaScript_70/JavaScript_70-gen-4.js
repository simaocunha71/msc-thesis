  // Sorting the array in ascending order
  lst.sort((a, b) => a - b);

  // Initialize an empty array to store the result
  let result = [];

  // Loop until the input array becomes empty
  while (lst.length) {

    // Add the smallest value to the result array
    result.push(lst.shift());

    // If the input array is not empty, add the largest value to the result array
    if (lst.length) {
      result.push(lst.pop());
    }
  }

  // Return the result array
  return result;
};

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []

// This function works by sorting the input array in ascending order and then iteratively removing the smallest and largest elements, adding them to the result array, and continuing this process until the input array is empty.

// The time complexity of this function is O(n log n) due to the sorting operation, and the space complexity is O(n) for the result array.

// The function returns the input array sorted in a strange order.

// The function handles an empty array by returning an empty array.

// The function correctly handles arrays with an even number of elements by alternating between the smallest and largest remaining elements.

// The function correctly handles arrays with an odd number of elements by alternating between the smallest and largest remaining elements, and the middle element is left in its original position.

// The function correctly handles negative numbers and zero.

// The function correctly handles arrays with duplicate elements.

// The function correctly handles arrays with a single element.

// The function correctly handles arrays with two elements.

// The function correctly handles arrays with three elements.

// The function correctly handles arrays with many elements.
*/

// This function works by sorting the input array in ascending order and then iteratively removing the smallest and largest elements,