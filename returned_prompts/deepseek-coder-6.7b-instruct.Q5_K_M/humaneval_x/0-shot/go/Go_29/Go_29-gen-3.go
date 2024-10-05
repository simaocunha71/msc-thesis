
// Define a function FilterByPrefix that takes an array of strings and a prefix as arguments.
func FilterByPrefix(strings []string, prefix string) []string {

    // Initialize an empty slice to store the filtered strings.
    var filteredStrings []string

    // Iterate over the input list of strings.
    for _, str := range strings {

        // Check if the current string starts with the given prefix.
        if strings.HasPrefix(str, prefix) {

            // If yes, append the string to the filteredStrings slice.
            filteredStrings = append(filteredStrings, str)
        }
    }

    // Return the filteredStrings slice.
    return filteredStrings
}

func main() {

    // Test the function.
    fmt.Println(FilterByPrefix([]string{}, "a")) // []
    fmt.Println(FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a")) // ["abc", "array"]
}

*/
package main

import (
	"fmt"
	"strings"
)

func FilterByPrefix(strings []string, prefix string) []string {

	var filteredStrings []string

	for _, str := range strings {
		if strings.HasPrefix(str, prefix) {
			filteredStrings = append(filteredStrings, str)
		}
	}

	return filteredStrings
}

func main() {
	fmt.Println(FilterByPrefix([]string{}, "a")) // []
	fmt.Println(FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a")) // ["abc", "array"]
}











































































































