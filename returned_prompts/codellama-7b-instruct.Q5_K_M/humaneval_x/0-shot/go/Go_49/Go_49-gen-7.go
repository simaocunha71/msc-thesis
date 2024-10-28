
// Return the sum of the values in the map.
// >>> Summation(map[string]int{"a":1, "b":2})
// 3
// >>> Summation(map[string]int{"a":1, "b":2, "c":3})
// 6
func Summation(m map[string]int) int {

B:

// Return the product of the values in the map.
// >>> Product(map[string]int{"a":1, "b":2})
// 2
// >>> Product(map[string]int{"a":1, "b":2, "c":3})
// 6
func Product(m map[string]int) int {

C:

// Return a slice of the map's keys.
// >>> Keys(map[string]int{"a":1, "b":2})
// []string{"a", "b"}
// >>> Keys(map[string]int{"a":1, "b":2, "c":3})
// []string{"a", "b", "c"}
func Keys(m map[string]int) []string {

D:

// Return a slice of the map's values.
// >>> Values(map[string]int{"a":1, "b":2})
// []int{1, 2}
// >>> Values(map[string]int{"a":1, "b":2, "c":3})
// []int{1, 2, 3}
func Values(m map[string]int) []int {

E:

// Return the length of the slice.
// >>> Length([]string{"a", "b"})
// 2
// >>> Length([]string{"a", "b", "c"})
// 3
// >>> Length([]int{1, 2, 3})
// 3
func Length(s interface{}) int {

F:

// Return the first element of the slice.
// >>> First([]string{"a", "b"})
// "a"
// >>> First([]int{1, 2, 3})
// 1