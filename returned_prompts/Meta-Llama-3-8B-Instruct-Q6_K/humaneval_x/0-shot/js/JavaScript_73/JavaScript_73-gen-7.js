Here is a JavaScript function that solves the problem:
```
const smallestChange = (arr) => {
  let left = 0;
  let right = arr.length - 1;
  let changes = 0;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
    }
    left++;
    right--;
  }

  return changes;
};
```
Here's an explanation of the code:

1. We initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
2. We initialize a counter, `changes`, to keep track of the number of changes needed.
3. We loop until `left` meets or exceeds `right`.
4. Inside the loop, we check if the elements at `left` and `right` are equal. If they're not, we increment `changes`.
5. We increment `left` and decrement `right` to move the pointers closer to the center of the array.
6. Finally, we return the total number of changes needed to make the array palindromic.

You can test this function with the examples you provided:
```
console.log(smallestChange([1,2,3,5,4,7,9,6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0
```
I hope this helps! Let me know if you have any questions. 😊

Edit: I realized that my initial solution was incorrect. Here's a corrected version:
```
const smallestChange = (arr) => {
  let changes = 0;
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
      let mid = Math.floor((left + right) / 2);
      if (arr[left] !== arr[mid]) {
        changes++;
      }
      if (arr[right] !== arr[mid]) {
        changes++;
      }
    }
    left++;
    right--;
  }

  return changes;
};
```
This solution correctly calculates the minimum number of changes needed to make the array palindromic. It works by iterating through the array from both ends and keeping track of the