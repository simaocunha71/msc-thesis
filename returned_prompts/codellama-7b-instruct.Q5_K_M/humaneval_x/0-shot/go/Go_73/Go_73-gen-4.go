
// Given a positive integer n, find the smallest number of perfect powers of n,
// that is, powers of the form a^b, such that a > 1, b > 1, and a^b = n.
//
// For example:
// SmallestNumberOfPerfectPowers(1) == 0
// SmallestNumberOfPerfectPowers(2) == 1
// SmallestNumberOfPerfectPowers(8) == 3
// SmallestNumberOfPerfectPowers(9) == 2
// SmallestNumberOfPerfectPowers(10) == 1
// SmallestNumberOfPerfectPowers(100) == 3
// SmallestNumberOfPerfectPowers(1000) == 5
func SmallestNumberOfPerfectPowers(n int) int {

B:

// Given an array of integers, find the index of the element that has the maximum difference between the sum of the elements on its left side and the sum of the elements on its right side. If there are multiple answers, return the smallest number.
//
// For example:
// MaxDiff([1, 2, 3, 4, 5]) == 3
// MaxDiff([1, 2, 3, 4, 5, 6]) == 5
// MaxDiff([1, 2, 3, 4, 5, 6, 7]) == 5
// MaxDiff([1, 2, 3, 4, 5, 6, 7, 8]) == 7
func MaxDiff(arr []int) int {

C:

// Given an array of integers, find the index of the element that has the minimum absolute difference between the sum of the elements on its left side and the sum of the elements on its right side. If there are multiple answers, return the smallest number.
//
// For example:
// MinAbsDiff([1, 2, 3, 4, 5]) == 0
// MinAbsDiff([1, 2, 3, 4, 5, 6]) == 1
// MinAbsDiff([1, 2, 3, 4,