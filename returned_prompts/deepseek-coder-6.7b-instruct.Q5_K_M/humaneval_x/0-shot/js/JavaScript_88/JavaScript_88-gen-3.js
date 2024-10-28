  if(array.length === 0) return array;
  
  let sortedArray = [...array];
  let sum = array[0] + array[array.length - 1];
  
  sortedArray.sort((a, b) => {
    if(sum % 2 === 0) {
      return b - a;
    } else {
      return a - b;
    }
  });
  
  return sortedArray;
}

console.log(sortArray([])) // []
console.log(sortArray([5])) // [5]
console.log(sortArray([2, 4, 3, 0, 1, 5])) // [0, 1, 2, 3, 4, 5]
console.log(sortArray([2, 4, 3, 0, 1, 5, 6])) // [6, 5, 4, 3, 2, 1, 0]

// This solution has a time complexity of O(n log n) due to the sort function and a space complexity of O(n) for the copy of the given array.
// In this solution, we are sorting the given array in ascending or descending order based on the sum of the first and last elements of the array.
// We are not changing the given array but returning a new sorted array.
// We are using the JavaScript's array sort method with a custom comparison function to sort the array.
// The comparison function compares the elements based on the sum of the first and last elements of the array.
// If the sum is even, we sort the array in descending order, else we sort the array in ascending order.
// We then return the sorted array.
// If the given array is empty, we return the array as it is.
// If the given array has only one element, we return the array as it is.
// We have tested the solution with the provided examples and it is working as expected.
// We have also tested the solution with some other examples to make sure it is working as expected.
*/

// This solution is correct and it is efficient. The time complexity is O(n log n) and the space complexity is O(n).
// The solution sorts the array in asc