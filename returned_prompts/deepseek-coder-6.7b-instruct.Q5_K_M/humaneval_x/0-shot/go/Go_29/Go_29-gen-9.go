
// Create an empty slice to hold the filtered strings
	result := make([]string, 0)

	// Iterate over the input strings
	for _, str := range strings {
		// If the string starts with the prefix, append it to the result slice
		if strings.HasPrefix(str, prefix) {
			result = append(result, str)
		}
	}

	// Return the result slice
	return result
}

*/
package main

import (
	"fmt"
	"strings"
)

func main() {
	strings := []string{"abc", "bcd", "cde", "array"}
	prefix := "a"
	fmt.Println(FilterByPrefix(strings, prefix))
}

func FilterByPrefix(strings []string, prefix string) []string {
	result := make([]string, 0)
	for _, str := range strings {
		if strings.HasPrefix(str, prefix) {
			result = append(result, str)
		}
	}
	return result
}
package main

import (
	"fmt"
)

/*
