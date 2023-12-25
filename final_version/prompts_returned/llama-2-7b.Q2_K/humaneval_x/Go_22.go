// Filter given list of any values only for integers
// >>> FilterIntegers(['a', 3.14, 5])
// [5]
// >>> FilterIntegers([1, 2, 3, 'abc', {}, []])
// [1, 2, 3]
func FilterIntegers(values []interface{}) []int {
	var integers []int
	for _, v := range values {
		if int64val, isInt := strconv.ParseInt(v.(string), 10, 64); !isInt && len(integers) == 0 {
			integers = append(integers, v...)
		} else if !strconv.Itoa(int64val).IsNumber() {
			return nil
		}
	}
	return integers
}

// FindFirstIndex implements a binary search for the first index of an element in an array where a boolean expression is true.
func FindFirstIndex(array []bool, element bool) int {
	var low, high, mid int
	if len(array) == 0 || array[0] != element {
		return -1
	}
	if len(array) > 1 && array[len(array)-1] == element {
		return len(array) - 1
	} else if len(array) == 1 {
		return len(array) - 1 // avoid division by zero error in the case of a single element in an array
	} else if array[0] != element {
		for low < high {
			mid = (low + high) / 2
			if !element == ArrayContains(mid, array...) {
				high = mid - 1 // go back and start dividing from this index
			} else {
				high = mid // we keep the current index as it contains element
			}
		}
	}
	if high != len(array)-1 && !element == ArrayContains(high+1, array...) { // avoid division by zero error in case we have to return something else than -1
		return -1
	} else {
		return