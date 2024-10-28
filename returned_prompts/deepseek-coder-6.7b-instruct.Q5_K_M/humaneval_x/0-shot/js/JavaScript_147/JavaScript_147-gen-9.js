  let arr = [];
  for (let i = 1; i <= n; i++) {
    arr.push(i * i - i + 1);
  }

  let cnt = Array(n).fill(0);
  for (let i = 0; i < n; i++) {
    for (let j = i - 1; j >= 0; j--) {
      if (arr[i] % arr[j] === 0) {
        cnt[i]++;
      }
    }
  }

  let sum = Array(n).fill(0);
  for (let i = 0; i < n; i++) {
    sum[i] = (i > 0 ? sum[i - 1] : 0) + cnt[i];
  }

  let ans = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
      ans += sum[j] * cnt[i] + (arr[i] % 3 === 0 ? cnt[i] : 0);
    }
  }
  return ans;
};


/* 
  Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
  Range sum S(i, j) is the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

  Example:
  Input: nums = [-2, 5, -1], lower = -2, upper = 2,
  Output: 3
  Explanation: The three ranges are : [0, 0], [2, 2], and [0, 2] and their respective sums are:
  -2, 5, and -3. Therefore, the sum of the ranges is 0, 5, and -3, which are all in the range [-2, 2].

*/

const countRangeSum = (nums, lower, upper) => {
  let n = nums.length;
  if (n === 0) return 0;
  
  let prefixSum = new Array