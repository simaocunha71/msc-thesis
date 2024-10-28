  let left = 0;
  let right = arr.length - 1;
  let counter = 0;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      counter++;
    }
    left++;
    right--;
  }

  return counter;
}

console.log(smallestChange([1,2,3,5,4,7,9,6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0

*/

*/

// Answer:

// The function `smallestChange` works by comparing the elements of the array from both ends. If the elements are not the same, it increments the counter by 1. It continues this process moving towards the center of the array. The final value of the counter is the minimum number of changes needed to make the array palindromic.

// For the array [1,2,3,5,4,7,9,6], the process would look like this:
// 1. Compare 1 (left) and 6 (right) - they're not the same, so increment counter by 1.
// 2. Move left pointer to 2 and right pointer to 5. They're the same, so move on.
// 3. Repeat the process with 2 (left) and 7 (right) - they're not the same, so increment counter by 1.
// 4. Move left pointer to 3 and right pointer to 4. They're the same, so move on.
// 5. Finally, left pointer is equal to right pointer, so the function returns the counter, which is 4.

// This approach has a time complexity of O(n/2), where n is the length of the array, because it only traverses half the array.

// This function can be optimized further by reducing the number of comparisons by checking if the array is already a palindrome from the start and if so, returning 0. This would make the