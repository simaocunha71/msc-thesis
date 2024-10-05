/*
  Given a non-empty array of integers arr, find the maximum of the sum of its
  first k non-empty subarrays.

  Example:

      Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
      Output: 24 # sum of 21 + 3

  Constraints:
      1. 1 <= len(arr) <= 100
      2. 1 <= k <= len(arr)
  */
const addElements = (arr, k) => {

  let max = 0;
  let sum = 0;

  for (let i = 0; i < k; i++) {
    sum += arr[i];
    max = Math.max(max, sum);
  }

  for (let i = k; i < arr.length; i++) {
    sum += arr[i];
    sum -= arr[i - k];
    max = Math.max(max, sum);
  }

  return max;
};
