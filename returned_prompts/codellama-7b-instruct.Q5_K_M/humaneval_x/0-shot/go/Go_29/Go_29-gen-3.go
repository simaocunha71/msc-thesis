
// Filter an input list of strings only for ones that end with a given suffix.
// >>> FilterBySuffix([], 'a')
// []
// >>> FilterBySuffix(['abc', 'bcd', 'cde', 'array'], 'e')
// ['cde', 'array']
func FilterBySuffix(strings []string, suffix string) []string {

B:

// Filter an input list of strings only for ones that contain a given substring.
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bcd', 'cde', 'array'], 'cd')
// ['bcd', 'cde']
func FilterBySubstring(strings []string, substring string) []string {

C:

// Filter an input list of integers only for ones that are greater than a given value.
// >>> FilterByValue([], 1)
// []
// >>> FilterByValue([1, 2, 3, 4, 5], 3)
// [4, 5]
func FilterByValue(ints []int, value int) []int {

D:

// Filter an input list of integers only for ones that are divisible by a given value.
// >>> FilterByDivisibility([], 1)
// []
// >>> FilterByDivisibility([1, 2, 3, 4, 5], 2)
// [2, 4]
func FilterByDivisibility(ints []int, divisor int) []int {

E:

// Filter an input list of floats only for ones that are greater than a given value.
// >>> FilterByValue([], 1.0)
// []
// >>> FilterByValue([1.0, 2.0, 3.0, 4.0, 5.0], 3.0)
// [4.0, 5.0]
func FilterByValue(floats []float64, value float64) []float64 {

F:

// Filter an input list of floats only for ones that are divisible by a given value.
// >>> FilterByDivisibility([], 1.0)
// []
