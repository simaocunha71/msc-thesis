
// Given a positive integer, find the next smallest positive integer divisible by all of the numbers from 1 to 20.
// Example:
// NextSmallestDivisible(199) == 200
// NextSmallestDivisible(197) == 198
// NextSmallestDivisible(196) == 196
func NextSmallestDivisible(n int) int {

B:

// Given a string s, return the number of different non-empty palindromic substrings in s,
// counting duplicates.
// A string is a palindrome when it reads the same backward as forward.
// A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
// For example, "ace" is a subsequence of "abcde" while "aec" is not.
// A subsequence of a string s is said to be palindromic if it is equal to the sequence obtained by reversing the sequence.
// For example, "abcba" is a palindromic subsequence of "abcba".
// Example 1:
// Input: s = "abc"
// Output: 3
// Explanation: Three palindromic substrings: "a", "b", "c".
// Example 2:
// Input: s = "aaa"
// Output: 6
// Explanation: Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".
// Example 3:
// Input: s = "aba"
// Output: 2
// Explanation: Two palindromic substrings: "a", "a".
// Constraints:
// 1 <= s.length <= 1000
// s consists only of lowercase English letters.
func CountSubstrings(s string) int {

C:

// Given a string s, return the number of substrings of s that meet the following conditions:
// The substrings do not overlap, and they are all distinct.
// Example 1:
// Input: s = "abcabcbb"
