To solve this problem we can follow the steps below:

1) Create an array called 'sorted' and assign the first element of the input
array 'arr' to it. We will use 'sorted' to keep track of the sorted elements
of the array 'arr' that we have found so far.

2) Create a variable called 'found' and assign the second element of the input
array 'arr' to it. We will use 'found' to keep track of the maximum element
of the array 'arr' that we have found so far.

3) Iterate through the remaining elements of the input array 'arr' starting from
the third element. For each element, check if it is greater than or equal to
the current maximum element 'found'. If it is, then append the current element
to the 'sorted' array and update the 'found' variable to the current element. If
it is not, then append the current element to the 'sorted' array and continue
to the next element of the input array 'arr'.

4) After iterating through all the elements of the input array 'arr', check if
the length of the 'sorted' array is equal to the length of the input array 'arr'.
If it is, then return true as all the elements of the input array 'arr' have been
found in sorted order. Otherwise, return false as some elements of the input
array 'arr' have not been found in sorted order.

5) If the input array 'arr' is empty, then return true as an empty array is considered
to be sorted.

6) If the above steps do not result in true, then return false.

*/

// Implement the above steps in code

const moveOneBall = (arr) => {
  if (arr.length === 0) {
    return true;
  }

  let sorted = [arr[0]];
  let found = arr[1];

  for (let i = 2; i < arr.length; i++) {
    if (arr[i] >= found) {
      sorted.push(arr[i]);
      found = arr[i];
    } else {
      sorted.push(arr[i]);
    }
  }

  return sorted.length === arr.