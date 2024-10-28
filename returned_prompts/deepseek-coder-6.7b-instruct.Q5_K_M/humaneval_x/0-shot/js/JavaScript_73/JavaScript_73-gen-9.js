  let changes = 0;
  let i = 0;
  let j = arr.length - 1;

  while (i < j) {
    if (arr[i] !== arr[j]) {
      changes++;
    }
    i++;
    j--;
  }

  return changes;
}
*/

// Test cases
console.log(smallestChange([1,2,3,5,4,7,9,6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0

/*
  Explanation:
  In the first test case, the array is not a palindrome and needs at least 4 changes:
  [1,2,3,5,4,7,9,6] => [1,2,3,4,4,3,2,1]
  In the second test case, the array is already a palindrome but there are two occurrences of '2' and '3',
  so we can remove one of them to make it a palindrome in one change:
  [1, 2, 3, 4, 3, 2, 2] => [1, 2, 3, 4, 3, 2]
  In the third test case, the array is already a palindrome, so no changes are needed.
  */

  // The solution works by comparing the elements from the start and the end of the array.
  // If they are not equal, a change is made (incrementing the changes counter) and then moving inward.
  // This continues until we have checked all pairs of elements.
  // The time complexity of this solution is O(n) as we are making a single pass through the array.
  // The space complexity is O(1) as we are only using a constant amount of space to store the changes counter and indices i and j.




























