```go
package main

import (
	"strconv"
	"strings"
)

// Return a string containing space-delimited numbers starting from 0 upto n inclusive.
// >>> StringSequence(0)
// '0'
// >>> StringSequence(5)
// '0 1 2 3 4 5'
func StringSequence(n int) string {
	var result strings.Builder
	for i := 0; i <= n; i++ {
		result.WriteString(strconv.Itoa(i))
		if i < n {
			result.WriteString(" ")
		}
	}
	return result.String()
}

func main() {
	fmt.Println(StringSequence(0))  // Output: 0
	fmt.Println(StringSequence(5))  // Output: 0 1 2 3 4 5
}
```


Explanation:
The given problem can be solved by creating a function named `StringSequence` that accepts an integer `n` as an argument. This function uses a `strings.Builder` to construct the result string.

The function iterates over the range from 0 to `n` (inclusive) using a for loop. Inside the loop, it converts each integer `i` to a string using `strconv.Itoa` and appends it to the `strings.Builder`.

After appending each integer, the function checks if `i` is less than `n`. If it is, it appends a space character to the `strings.Builder` to separate the integers. If `i` is equal to `n`, it means we're at the last integer, so we don't need to append a space.

Finally, the function returns the string representation of the `strings.Builder` using the `String` method.

In the `main` function, we call `StringSequence` with arguments 0 and 5 and print the results. The output is as expected: "0" for `StringSequence(0)` and "0 1 2 3 4 5" for `StringSequence(5)`.