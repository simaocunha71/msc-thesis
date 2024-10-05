    arr.sort(function(a, b) {return a - b;});
    return arr.slice(0, k);
};


/*
  Given an array of integers, find the pair of integers with the maximum difference.
  Return a pair of integers as an array. If there are multiple pairs with the same max difference, return any of them.

  Example 
  Input: {3, 7, 9, 10, 12, 13}
  Output: [12, 13]

  Note:
  The length of the array will be in the range of [1, 10000].
  The elements in the array will be in the range of [1, 100000].
  The pair of integers with the maximum difference will be unique and exist only one in the array.
 */
const maximumDifference = (arr) => {
    let max = 0;
    let m1 = 0;
    let m2 = 0;

    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] - arr[i] > max) {
                max = arr[j] - arr[i];
                m1 = arr[i];
                m2 = arr[j];
            }
        }
    }
    return [m1, m2];
};


/*
  Given a string, find the longest substring which contains only one type of character.
  That is, a substring is longests if and only if all characters in the substring are the same.
  Return the length of this substring.

  Example 
  Input: "abcbababac"
  Output: 5

  Note:
  The length of the string will be in the range of [1, 10000].
 */
const longestSubstring = (s) => {
    let max = 0;
    let l = 1;

    for (let i = 0; i < s.length - 1; i++) {
