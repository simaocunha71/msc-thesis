// Filter given list of any values only for strings
// >>> FilterStrings(['a', 3.14, 5])
// ['a']
// >>> FilterStrings([1, 2, 3, 'abc', {}, []])
// ['abc']
func FilterStrings(values []interface{}) []string {

B:
// Filter given list of any values only for booleans
// >>> FilterBooleans(['a', 3.14, 5])
// []
// >>> FilterBooleans([true, false, 1, 0, 'abc', {}, []])
// [true, false, 1, 0]
func FilterBooleans(values []interface{}) []bool {

C:
// Filter given list of any values only for maps
// >>> FilterMaps(['a', 3.14, 5])
// []
// >>> FilterMaps([{}, {'a': 1}, [1, 2, 3]])
// [{}, {'a': 1}]
func FilterMaps(values []interface{}) []map[string]interface{} {

D:
// Filter given list of any values only for slices
// >>> FilterSlices(['a', 3.14, 5])
// []
// >>> FilterSlices([{}, {'a': 1}, [1, 2, 3]])
// [[1, 2, 3]]
func FilterSlices(values []interface{}) [][]interface{} {

E:
// Filter given list of any values only for functions
// >>> FilterFunctions(['a', 3.14, 5])
// []
// >>> FilterFunctions([func(x int) int { return x }, func(x string) string { return x }])
// [func(x int) int]
func FilterFunctions(values []interface{}) []func(interface{}) interface{} {

F:
// Filter given list of any values only for channels
// >>> FilterChannels(['a', 3.14, 5])
// []
// >>> FilterChannels([make(chan int), make(chan string)])
// [make(chan int)]
func FilterChannels(values []interface{}) []chan interface{} {

