To solve this problem, we need to find a sequence of right shifts that will result in a sorted array. We can do this by finding the largest index i such that arr[i] is less than arr[i + 1]. This means that if we shift arr[i] to the left, we will get a smaller element in the last position. Then, we need to find the largest index j such that arr[j] is greater than arr[j + 1]. This means that if we shift arr[j] to the left, we will get a larger element in the last position. We can repeat this process until we reach the end of the array.

Here is a step-by-step explanation of the solution:

1. Initialize a variable `i` to the length of the array minus one. This will be the index of the last element in the array.

2. While `i` is greater than or equal to zero, do the following:
   a. If the current element `arr[i]` is less than the next element `arr[i + 1]`, increment `i` by one. This means that if we shift `arr[i]` to the left, we will get a smaller element in the last position.
   b. If the current element `arr[i]` is greater than the next element `arr[i + 1]`, set the result to `false` and break out of the loop. This means that it is impossible to get a non-decreasing order by performing any number of right shift operations.

3. If `i` is less than zero, return `true`, as this means that all elements in the array are greater than the next element, so we can obtain a non-decreasing order by shifting all elements to the left.

4. Otherwise, return `false`, as we have found a sequence of elements that cannot be sorted by shifting elements to the left.

The time complexity of this solution is O(n), where n is the length of the array.

*/

// Solution

function moveOneBall(arr) {
  let i = arr.length - 1;
  while (i >= 0) {
    if (arr[i] < arr[i + 1]) {
      i++;
    } else {
      return false;
   