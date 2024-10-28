
// You are given a sorted array of integers. You need to find the maximum sum of the elements that can be chosen from the array.
// If there are no elements in the array, return 0.
// 
// Example:
// Input: arr = [1, 2, 3, 4]
// Output: 10
// Explanation:
// The maximum sum is obtained when all four elements are chosen: 1 + 2 + 3 + 4 = 10.
func GetMaxSum(arr []int) int {

B:

// A number is considered lucky if the sum of its digits is divisible by 2 or 5.
// Given a number n, return the lucky number that sums up to n. If there is no such number, return -1.
// 
// Example:
// Input: n = 1230
// Output: 356
// Explanation: 12 + 30 = 356 is a lucky number.
func GetLuckyNumber(n int) int {

C:

// Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest sum.
// Return the maximum sum.
// 
// Example:
// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
func GetMaxSum(nums []int) int {

D:

// Given two integers, find the next greater number that is not in the array.
// For example, given array [1, 2, 3, 4] and target value 3, return 4.
// Given array [1, 2, 3, 4] and target value 5, return -1.
func GetNextGreaterNumber(nums []int, target int) int {

E:

// Given an array of integers, find the first missing positive integer in linear time and constant space.
// In other words, find the lowest positive integer that does not exist in the array.
// The array can contain duplicates