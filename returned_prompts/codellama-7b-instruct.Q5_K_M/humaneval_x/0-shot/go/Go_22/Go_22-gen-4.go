// Filter given list of any values only for strings
// >>> FilterStrings(['a', 3.14, 5])
// ['a']
// >>> FilterStrings([1, 2, 3, 'abc', {}, []])
// ['abc']
func FilterStrings(values []interface{}) []string {

B:
// Filter given list of any values only for floats
// >>> FilterFloats([1, 2, 3, 'abc', {}, []])
// [3.14]
func FilterFloats(values []interface{}) []float64 {

C:
// Filter given list of any values only for maps
// >>> FilterMaps([1, 2, 3, 'abc', {}, []])
// [{}]
func FilterMaps(values []interface{}) []map[string]interface{} {

D:
// Filter given list of any values only for lists
// >>> FilterLists([1, 2, 3, 'abc', {}, []])
// [[], []]
func FilterLists(values []interface{}) [][]interface{} {

E:
// Filter given list of any values only for bools
// >>> FilterBools([1, 2, 3, 'abc', {}, []])
// [true, false, false]
func FilterBools(values []interface{}) []bool {

F:
// Filter given list of any values only for ints
// >>> FilterInts([1, 2, 3, 'abc', {}, []])
// [1, 2, 3]
func FilterInts(values []interface{}) []int {

G:
// Filter given list of any values only for bools
// >>> FilterInts([1, 2, 3, 'abc', {}, []])
// [1, 2, 3]
func FilterInts(values []interface{}) []int {

H:
// Filter given list of any values only for floats
// >>> FilterFloats([1, 2, 3, 'abc', {}, []])
// [3.14]
func FilterFloats(values []interface{}) []float64 {

I:
// Filter given list of any values only for maps