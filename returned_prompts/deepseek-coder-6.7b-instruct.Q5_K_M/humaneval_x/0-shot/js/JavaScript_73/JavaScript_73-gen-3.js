  let changes = 0;
  let left = 0;
  let right = arr.length - 1;
  
  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
    }
    left++;
    right--;
  }
  
  return changes;
};

console.log(smallestChange([1,2,3,5,4,7,9,6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0

// In this solution, we're using a two-pointer approach to compare the elements at the ends of the array. 
// If they're not the same, we increment the changes counter and move both pointers. If they're the same, we move both pointers. 
// We stop when the left pointer is no longer less than the right pointer. 
// This gives us the minimum number of changes required to make the array palindromic.

// The time complexity of this solution is O(n), where n is the length of the array, as we're iterating through the array once. 
// The space complexity is O(1), as we're using a constant amount of space.

// Note: This solution assumes that the array is not empty. If the array can be empty, you should add a check for this before the while loop.



















































































































































