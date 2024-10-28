/*
  Given a non-empty array of integers arr and an integer k, return
  the sum of the elements with at most k digits from the first k elements of arr.

  Example:

      Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
      Output: 24 # sum of 21 + 3

  Constraints:
      1. 1 <= len(arr) <= 100
      2. 1 <= k <= len(arr)
  */
const addElements = (arr, k) => {
    let sum = 0;
    for (let i = 0; i < k; i++) {
        sum += arr[i];
    }
    return sum;
}

