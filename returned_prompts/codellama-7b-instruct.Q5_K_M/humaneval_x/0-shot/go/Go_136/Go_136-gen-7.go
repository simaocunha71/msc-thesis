
// Create a function that returns a slice of the first 'n' elements
// of a list, where 'n' is a positive integer.
// If 'n' is greater than the length of the list, return the entire list.
// 
// Examples:
// FirstN([1, 2, 3, 4, 5], 2) == [1, 2]
// FirstN([1, 2, 3, 4, 5], 10) == [1, 2, 3, 4, 5]
// FirstN([1, 2, 3, 4, 5], 0) == []
func FirstN(lst []int, n int) []int {

B:

// Create a function that returns a slice of the last 'n' elements
// of a list, where 'n' is a positive integer.
// If 'n' is greater than the length of the list, return the entire list.
// 
// Examples:
// LastN([1, 2, 3, 4, 5], 2) == [4, 5]
// LastN([1, 2, 3, 4, 5], 10) == [1, 2, 3, 4, 5]
// LastN([1, 2, 3, 4, 5], 0) == []
func LastN(lst []int, n int) []int {

C:

// Create a function that returns a list of the elements of a list,
// in reverse order.
// 
// Examples:
// Reverse([]) == []
// Reverse([1]) == [1]
// Reverse([1, 2, 3]) == [3, 2, 1]
func Reverse(lst []int) []int {

D:

// Create a function that returns a list of the elements of a list,
// in reverse order, while maintaining their order of appearance.
// 
// Examples:
// ReverseOrder([]) == []
// ReverseOrder([1]) == [1]
// ReverseOrder([1, 2, 3]) == [3, 2, 