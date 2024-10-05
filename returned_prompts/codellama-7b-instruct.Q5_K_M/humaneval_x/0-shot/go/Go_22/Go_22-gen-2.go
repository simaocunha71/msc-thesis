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
// [3.14]
func FilterFloats(values []interface{}) []float64 {

C:
// Filter given list of any values only for booleans
// >>> FilterBooleans(['a', 3.14, 5])
// []
// >>> FilterBooleans([true, false, 1, 0, 'abc', {}, []])
// [true, false]
func FilterBooleans(values []interface{}) []bool {

D:
// Filter given list of any values only for arrays
// >>> FilterArrays(['a', 3.14, 5])
// []
// >>> FilterArrays([[1, 2, 3], ['a', 'b'], 5])
// [[1, 2, 3], ['a', 'b']]
func FilterArrays(values []interface{}) [][]interface{} {

E:
// Filter given list of any values only for maps
// >>> FilterMaps(['a', 3.14, 5])
// []
// >>> FilterMaps([{'a': 1}, {'b': 2}, 5])
// [{'a': 1}, {'b': 2}]
func FilterMaps(values []interface{}) []map[string]interface{} {
```

# Usage
```go
// Example usage of function FilterIntegers()
package main

import (
    "fmt"
)

func main() {
    fmt.Println(FilterIntegers([]interface{}{1, 2.0, 3, "abc", {}, []}))
    // [1, 