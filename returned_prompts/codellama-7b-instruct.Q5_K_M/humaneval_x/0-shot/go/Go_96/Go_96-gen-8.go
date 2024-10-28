
// Implement a function that takes an array of integers and returns a new array of integers
// where each element is the product of an element in the original array and each of the
// elements that follow it in the original array.
// for example:
// Products([1, 2, 3]) => [1, 2*1, 2*2, 2*3, 3*1, 3*2, 3*3]
// Products([1, 2, -1]) => [1, 2*1, 2*2, 2*(-1), (-1)*1, (-1)*2]
// Products([1]) => [1]
// Products([1, 2, 3, 4]) => [1, 2*1, 2*2, 2*3, 2*4, 3*1, 3*2, 3*3, 3*4, 4*1, 4*2, 4*3, 4*4]
// Products([]) => []
func Products(arr []int) []int {

B:

// Implement a function that takes an array of integers and returns a new array of integers
// where each element is the sum of an element in the original array and each of the
// elements that follow it in the original array.
// for example:
// Sums([1, 2, 3]) => [1, 2+1, 2+2, 2+3, 3+1, 3+2, 3+3]
// Sums([1, 2, -1]) => [1, 2+1, 2+2, 2+(-1), (-1)+1, (-1)+2]
// Sums([1]) => [1]
// Sums([1, 2, 3, 4]) => [1, 2+1, 2+2, 2+3, 2+4, 3+1, 3+2, 3+3, 3+4, 4+1, 4+2, 4+3, 4+4]
// Sums([]) => []
func Sums(arr []int)