// Filter given list of any values only for integers
// >>> FilterIntegers(['a', 3.14, 5])
// [5]
// >>> FilterIntegers([1, 2, 3, 'abc', {}, []])
// [1, 2, 3]
func FilterIntegers(values []interface{}) []int {
	var i int
	for _, v := range values {
		switch t := v.(type) {
		case float64:
		case bool:
		}
	}
	return append([]int{}, values...)
}
