
	// Initialize length to 0
	var length int = 0

	// Iterate over the string
	for _, char := range str {
		length++
	}

	return length
}

In this implementation of Strlen function, we use range loop to iterate over the given string. Each character in the string is assigned to char variable, and length variable is incremented by 1 for each character. Once the loop is finished, length variable holds the length of the given string, and it is returned as the result of the function.

This implementation has time complexity O(n), where n is the length of the input string. This is because we need to iterate over the whole string to calculate its length.

For example, given the input "abc", the function will return 3, because there are 3 characters in the string.

This implementation is simple and straightforward, but it may not be the most efficient solution if you need to calculate the length of very large strings, as it requires iterating over the entire string. However, it is suitable for most cases, especially when the length of the string is relatively small.

Note: In Go programming language, the range loop iterates over the characters of a string. The underscore (_) is used as a blank identifier to ignore the index of each character.

// Return length of given string
// >>> Strlen('')
// 0
// >>> Strlen('abc')
// 3
func Strlen(str string) int {

	// Initialize length to 0
	var length int = 0

	// Iterate over the string
	for _, char := range str {
		length++
	}

	return length
}

In this implementation of Strlen function, we use range loop to iterate over the given string. Each character in the string is assigned to char variable, and length variable is incremented by 1 for each character. Once the loop is finished, length variable holds the length of the given string, and it is returned as the result of the function.

This implementation has time complexity O(n), where n is the length of the input string. This is because we need to iterate over the whole string to calculate its length.

For example, given the input "abc", the function will return 3, because there are 