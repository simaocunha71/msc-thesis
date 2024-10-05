
// Return true if the list is empty.
// >>> IsEmpty([])
// true
// >>> IsEmpty([1])
// false
func IsEmpty(l []int) bool {

B:

// Return the last number in the list.
// >>> Last([1, 2, 4, 10])
// 10
// >>> Last([10, 20, 30, 40])
// 40
func Last(l []int) int {

C:

// Return the list with the first number removed.
// >>> Tail([1, 2, 4, 10])
// [2, 4, 10]
// >>> Tail([10, 20, 30, 40])
// [20, 30, 40]
func Tail(l []int) []int {

D:

// Return the first number in the list.
// >>> Head([1, 2, 4, 10])
// 1
// >>> Head([10, 20, 30, 40])
// 10
func Head(l []int) int {

E:

// Return the list with the last number removed.
// >>> Init([1, 2, 4, 10])
// [1, 2, 4]
// >>> Init([10, 20, 30, 40])
// [10, 20, 30]
func Init(l []int) []int {

F:

// Return the list with the number added to the end.
// >>> Cons(10, [1, 2, 4])
// [1, 2, 4, 10]
// >>> Cons(40, [10, 20, 30])
// [10, 20, 30, 40]
func Cons(n int, l []int) []int {

G:

// Return the length of the list.
// >>> Length([1, 2, 4, 10])
// 4
// >>> Length([])