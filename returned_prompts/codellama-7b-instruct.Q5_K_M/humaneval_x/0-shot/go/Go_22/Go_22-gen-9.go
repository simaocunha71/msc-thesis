// Filter given list of any values only for strings
// >>> FilterStrings(['a', 3.14, 5])
// ['a']
// >>> FilterStrings([1, 2, 3, 'abc', {}, []])
// ['abc']
func FilterStrings(values []interface{}) []string {

B:
// Filter given list of any values only for floats
// >>> FilterFloats(['a', 3.14, 5])
// [3.14]
// >>> FilterFloats([1, 2, 3, 'abc', {}, []])
// []
func FilterFloats(values []interface{}) []float64 {

C:
// Filter given list of any values only for booleans
// >>> FilterBooleans(['a', 3.14, 5])
// []
// >>> FilterBooleans([1, 2, 3, 'abc', {}, []])
// []
func FilterBooleans(values []interface{}) []bool {

D:
// Filter given list of any values only for maps
// >>> FilterMaps(['a', 3.14, 5])
// []
// >>> FilterMaps([1, 2, 3, 'abc', {}, []])
// [map[interface {}]interface {}{}]
func FilterMaps(values []interface{}) []map[interface{}]interface{} {

E:
// Filter given list of any values only for arrays
// >>> FilterArrays(['a', 3.14, 5])
// []
// >>> FilterArrays([1, 2, 3, 'abc', {}, []])
// [[]]
func FilterArrays(values []interface{}) [][]interface{} {

F:
// Filter given list of any values only for nil values
// >>> FilterNil(['a', 3.14, 5])
// []
// >>> FilterNil([1, 2, 3, 'abc', {}, []])
// [<nil>]
func FilterNil(values []interface{}) []interface{} {

G:
// Filter given list of any values only for functions
// >>> FilterFunctions(['a', 3.14, 5])
