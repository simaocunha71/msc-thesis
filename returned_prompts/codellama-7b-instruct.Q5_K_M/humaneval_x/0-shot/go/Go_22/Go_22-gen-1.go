// Filter given list of any values only for integers
// >>> FilterIntegers(['a', 3.14, 5])
// [5]
// >>> FilterIntegers([1, 2, 3, 'abc', {}, []])
// [1, 2, 3]
func FilterIntegers(values []interface{}) []int {
	var integers []int
	for _, value := range values {
		switch value.(type) {
		case int:
			integers = append(integers, value.(int))
		case float64:
			if value.(float64) == float64(int(value.(float64))) {
				integers = append(integers, int(value.(float64)))
			}
		}
	}
	return integers
}
