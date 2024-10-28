
// Return true if the list l contains a number divisible by d.
// >>> DivisibleBy([1, 2, 3, 4, 5], 2)
// true
// >>> DivisibleBy([1, 3, 5, 7, 9], 2)
// false
func DivisibleBy(l []int, d int) bool {

B:

// Return the list of numbers in the list l that are below t.
// >>> BelowThreshold([1, 2, 4, 10], 100)
// [1, 2, 4]
// >>> BelowThreshold([1, 20, 4, 10], 5)
// [1, 4]
func BelowThreshold(l []int,t int) []int {

C:

// Return the list of numbers in the list l that are not divisible by d.
// >>> DivisibleBy([1, 2, 3, 4, 5], 2)
// [1, 3, 5]
// >>> DivisibleBy([1, 3, 5, 7, 9], 2)
// [1, 5, 7, 9]
func DivisibleBy(l []int, d int) []int {

D:

// Return the list of numbers in the list l that are between a and b (inclusive).
// >>> Between([1, 2, 4, 10], 2, 4)
// [2, 4]
// >>> Between([1, 2, 4, 10], 2, 10)
// [2, 4, 10]
func Between(l []int, a, b int) []int {

E:

// Return the list of numbers in the list l that are not between a and b (exclusive).
// >>> NotBetween([1, 2, 4, 10], 2, 4)
// [1, 10]
// >>> NotBetween([1, 2, 4, 10], 2, 10)
// [1]