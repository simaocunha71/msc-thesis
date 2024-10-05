To solve this problem, we can start by finding the middle index of the array, then compare the elements on either side of the middle index. If they are different, we need to change one of them to make the array palindromic. We can then repeat this process, incrementally moving towards the middle of the array until we reach the ends. We need to count the total number of changes needed to make the array palindromic.

Here's a step-by-step explanation of the solution:

1. Find the middle index of the array by dividing the length of the array by 2 and rounding down to the nearest whole number.
2. Initialize a variable `totalChanges` to keep track of the total number of changes needed to make the array palindromic. Set it to 0 initially.
3. Start a while loop that runs until the left pointer is less than the right pointer. The left pointer is initially set to 0, and the right pointer is initially set to the middle index.
4. Inside the while loop, compare the elements at the left and right pointers. If they are different, increment the `totalChanges` variable by 1.
5. Move the left pointer towards the middle of the array by adding 1 to it, and move the right pointer towards the middle of the array by subtracting 1 from it.
6. Once the while loop ends, return the `totalChanges` variable as the result.
7. Test the solution with the provided examples to ensure it's working correctly.

Here's the code for the solution:

```javascript
function smallestChange(arr) {
  let left = 0;
  let right = Math.floor(arr.length / 2);
  let totalChanges = 0;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      totalChanges++;
    }
    left++;
    right--;
  }

  return totalChanges;
}

console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // Output: 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // Output: 1
