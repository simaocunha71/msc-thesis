
// Implement a function that takes in an array of integers and returns an array of
// arrays, where each inner array contains all elements that are either in the
// same position or have the same value in the original array, for example:
// Group([1, 2, 3, 4, 5, 6]) => [[1, 2, 3], [4, 5, 6]]
// Group([1, 2, 3, 3, 4, 5, 6]) => [[1, 2, 3], [3, 4, 5], [6]]
// Group([1, 2, 2, 2, 3, 4, 5, 6]) => [[1], [2, 2, 2], [3], [4], [5], [6]]
// Group([1, 2, 3, 4, 5, 6]) => [[1], [2], [3], [4], [5], [6]]
func Group(arr []int) [][]int {

B:

// Implement a function that takes in an array of arrays and returns a new
// array containing all the elements from the original array of arrays in a
// random order, for example:
// Shuffle([[1, 2], [3, 4], [5, 6]]) => [3, 1, 5, 2, 4, 6]
// Shuffle([[1, 2], [3, 4], [5, 6], [7, 8]]) => [5, 1, 7, 2, 4, 8, 6]
// Shuffle([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) => [7, 1, 9, 2, 4, 8, 6, 10]
// Shuffle([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]) => [9, 1, 11, 2, 4, 8, 6, 10,