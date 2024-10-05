// Filter given list of any values only for floats
// >>> FilterFloats(['a', 5, 3.14])
// [3.14]
// >>> FilterFloats([1, 2, 3, 'abc', {}, []])
// []
func FilterFloats(values []interface{}) []float64 {

B:
// Filter given list of any values only for strings
// >>> FilterStrings(['a', 5, 3.14])
// ['a']
// >>> FilterStrings([1, 2, 3, {}, []])
// []
func FilterStrings(values []interface{}) []string {

C:
// Filter given list of any values only for booleans
// >>> FilterBooleans(['a', 5, 3.14])
// []
// >>> FilterBooleans([true, false, 1, 0, 'abc', {}, []])
// [true, false, 1, 0]
func FilterBooleans(values []interface{}) []bool {

D:
// Filter given list of any values only for maps
// >>> FilterMaps(['a', 5, 3.14])
// []
// >>> FilterMaps([{a: 1}, {b: 2}, {c: 3}, 'abc', {}, []])
// [{a: 1}, {b: 2}, {c: 3}]
func FilterMaps(values []interface{}) []map[string]interface{} {

E:
// Filter given list of any values only for slices
// >>> FilterSlices(['a', 5, 3.14])
// []
// >>> FilterSlices([{a: 1}, {b: 2}, {c: 3}, 'abc', {}, []])
// [{a: 1}, {b: 2}, {c: 3}, 'abc', {}]
func FilterSlices(values []interface{}) [][]interface{} {

F:
// Filter given list of any values only for functions
// >>> FilterFunctions(['a', 5, 3.14])
// []
// >>> FilterFunctions([add, subtract, multiply, divide, 'abc', {}, []