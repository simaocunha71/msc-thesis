/*
  You are given an array of integers, and a number k.
  Your task is to return the number of pairs of integers in the array that sum up to k.
  For example, if the input is [1, 2, 3, 4, 5, 6], and k is 7, then the output should be 2,
  because there are two pairs that sum up to 7: [5, 2] and [3, 4].
  If there are no pairs, return 0.
  Examples:
      pairs([1, 2, 3, 4, 5, 6], 7) == 2
      pairs([1, 2, 3, 4, 5, 6], 1) == 0
      pairs([1, 2, 3, 4, 5, 6], 3) == 1
  */
const pairs = (arr, k) => {

