/*
  Given an array arr of integers, return the length of the longest 
  non-decreasing subsequence.

  A subsequence is obtained by deleting some number of elements 
  from the array, leaving the remaining elements in their original order.

  Example 1:

      Input: arr = [4,2,3]
      Output: 3

  Example 2:

      Input: arr = [4,2,3,4,5,1,2,3,4]
      Output: 4

  Note:
      1. 1 <= arr.length <= 1000
      2. 0 <= arr[i] <= 1000
*/
const longestSubsequence = (arr) => {

B:
/*
  Given an integer n, return the nth Fibonacci number.

  The Fibonacci numbers are defined as:

      F1 = 0, F2 = 1, F3 = F1 + F2, F4 = F2 + F3, ...

  Example 1:

      Input: n = 2
      Output: 1

  Example 2:

      Input: n = 3
      Output: 2

  Example 3:

      Input: n = 4
      Output: 3

  Example 4:

      Input: n = 5
      Output: 5

  Example 5:

      Input: n = 10
      Output: 55

  Note:
      1. 0 <= n <= 100
*/
const nthFibonacci = (n) => {

C:
/*
  Given an array of integers arr, and two integers k1 and k2, where k1 <= k2.
  Return the maximum value of:

      sum(i) = (i ^ k1) + (i ^ k2) + ... + (i ^ k)

  where 0 <= i < arr.length.

  Example 1:

      Input: arr = [1,2,3,4,5], k1 = 2, k2 = 3
      Output: 