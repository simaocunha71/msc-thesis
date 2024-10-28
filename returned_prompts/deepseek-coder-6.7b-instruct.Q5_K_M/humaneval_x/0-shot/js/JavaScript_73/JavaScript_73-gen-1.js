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
}
*/

/*
  Explanation:
  This function works by using a two pointer technique where one pointer starts from the beginning of the array and the other from the end.
  It then compares the elements at these two pointers and if they are not equal, it increments a counter variable. This represents the number of changes needed to make the array palindromic.
  The pointers then move towards the center of the array. This process continues until the two pointers meet or cross each other.
  Finally, it returns the count of changes which represents the minimum number of changes needed to make the array palindromic.
 */

// Test Cases
console.log(smallestChange([1,2,3,5,4,7,9,6])) //== 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])) //== 1
console.log(smallestChange([1, 2, 3, 2, 1])) //== 0


// Expected Output
// 4
// 1
// 0
















































































































































































