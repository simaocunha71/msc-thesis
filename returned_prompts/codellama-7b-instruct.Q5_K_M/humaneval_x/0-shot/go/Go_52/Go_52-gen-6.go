
// Return the product of all the numbers in the list l.
// >>> Product([1, 2, 4, 10])
// 40
// >>> Product([1, 2, 4, -10])
// -40
func Product(l []int) int {

B:

// Return the list l without its first element.
// >>> Tail([1, 2, 4, 10])
// [2, 4, 10]
// >>> Tail([1])
// []
func Tail(l []int) []int {

C:

// Return the sum of all the numbers in the list l.
// >>> Sum([1, 2, 4, 10])
// 17
// >>> Sum([1, 2, 4, -10])
// -6
func Sum(l []int) int {

D:

// Return the last element in the list l.
// >>> Last([1, 2, 4, 10])
// 10
// >>> Last([1])
// 1
func Last(l []int) int {

E:

// Return true if all elements in the list l are above threshold t.
// >>> AboveThreshold([1, 2, 4, 10], 1)
// true
// >>> AboveThreshold([1, 2, 4, 10], 100)
// false
func AboveThreshold(l []int,t int) bool {

F:

// Return true if all elements in the list l are below or equal to threshold t.
// >>> BelowOrEqualToThreshold([1, 2, 4, 10], 10)
// true
// >>> BelowOrEqualToThreshold([1, 2, 4, 10], 1)
// false
func BelowOrEqualToThreshold(l []int,t int) bool {

G:

// Return true if all elements in the list l are below threshold t.
// >>> BelowThreshold([1, 2, 4, 10], 100)
// true
// >>> BelowThreshold