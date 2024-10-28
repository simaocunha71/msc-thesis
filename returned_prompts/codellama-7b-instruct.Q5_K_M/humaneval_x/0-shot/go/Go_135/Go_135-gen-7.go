
// Create a function which takes an array of integers and returns a new
// array containing all of the elements which are not greater than or equal to
// the element immediately preceding it. If no such element exists then return
// an empty array. The given array will not contain duplicate values.
// 
// Examples:
// CanArrange([1,2,4,3,5]) = [1,2,3]
// CanArrange([1,2,3]) = []
func CanArrange(arr []int) []int {

	// Initialize an empty array to store the result.
	result := []int{}

	// Loop through the array and compare each element to the previous
	// element. If the current element is not greater than or equal to the
	// previous element then add it to the result array.
	for i := 0; i < len(arr); i++ {
		if i == 0 {
			result = append(result, arr[i])
		} else {
			if arr[i] <= arr[i-1] {
				result = append(result, arr[i])
			}
		}
	}

	// Return the result array.
	return result
}

// Create a function which takes a string and an integer and returns a new
// string which is the original string repeated the specified number of times.
// If the repeat count is less than 1 then return the empty string.
// 
// Examples:
// RepeatString("abc", 3) = "abcabcabc"
// RepeatString("xyz", 2) = "xyzxyz"
// RepeatString("123", 0) = ""
func RepeatString(str string, count int) string {

	// Initialize an empty string to store the result.
	result := ""

	// Loop through the specified number of times and append the original
	// string to the result string.
	for i := 0; i < count; i++ {
		result += str
	}

	// Return the result string.
	return result
}

// Create a function which takes a string and returns a new string which is
// the original string