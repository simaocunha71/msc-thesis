Here is a JavaScript function that solves the problem:
```
const smallestChange = (arr) => {
  const n = arr.length;
  let count = 0;
  let left = 0;
  let right = n - 1;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      count++;
      left++;
      right--;
    } else {
      left++;
      right--;
    }
  }

  return count;
};
```
Here's an explanation of the code:

* We initialize a count variable to 0, which will keep track of the minimum number of changes needed to make the array palindromic.
* We initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
* We enter a loop that continues until `left` meets or exceeds `right`.
* Inside the loop, we check if the elements at `left` and `right` are equal. If they are not, we increment the count and move both pointers towards the center of the array.
* If the elements are equal, we simply move both pointers towards the center of the array.
* Once the loop exits, we return the count, which represents the minimum number of changes needed to make the array palindromic.

You can test the function with the examples you provided:
```
console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // Output: 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // Output: 1
console.log(smallestChange([1, 2, 3, 2, 1])); // Output: 0
```
I hope this helps! Let me know if you have any further questions.