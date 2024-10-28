
// Given a sorted array of integers, find the first index where the element
// changes from less than the previous element to greater than the previous
// element. If there is no such index, return the length of the array.
// Example:
// FirstGreater([]int{1, 2, 3, 4, 5}) == 3
// FirstGreater([]int{1, 1, 1, 1, 1}) == 5
func FirstGreater(nums []int) int {

B:

// Given an array of integers, find the first pair of integers that sum up to
// a given target value. If there is no such pair, return -1.
// Example:
// FirstPair([]int{1, 2, 3, 4, 5, 6}, 7) == 1, 2
// FirstPair([]int{1, 2, 3, 4, 5, 6}, 100) == -1
func FirstPair(nums []int, target int) (int, int) {

C:

// Given a string, find the first character that is not a space character or
// a letter. If there is no such character, return -1.
// Example:
// FirstNonSpaceLetter("hello world") == -1
// FirstNonSpaceLetter("   hello world") == -1
// FirstNonSpaceLetter("hello world   ") == -1
// FirstNonSpaceLetter("   hello world   ") == -1
// FirstNonSpaceLetter("hello world!") == 0
// FirstNonSpaceLetter("   hello world!") == 0
// FirstNonSpaceLetter("hello world!   ") == 0
// FirstNonSpaceLetter("   hello world!   ") == 0
// FirstNonSpaceLetter("   hello world!   ") == 0
func FirstNonSpaceLetter(s string) int {

D:

// Given two strings, find the first character that differs between the two
// strings. If there is no such character, return -1.
// Example:
// FirstDifference("hello", "hello") == -1
// FirstDifference("hello", "world") == 0