
    // Create an empty slice to store the filtered strings.
    var filtered []string

    // Loop through the input strings.
    for _, s := range strings {

        // Check if the current string starts with the given prefix.
        if strings.HasPrefix(s, prefix) {

            // If it does, append it to the filtered slice.
            filtered = append(filtered, s)
        }
    }

    // Return the filtered slice.
    return filtered
}

*/

package main

import (
	"fmt"
	"strings"
)

func FilterByPrefix(strings []string, prefix string) []string {
	var filtered []string

	for _, s := range strings {
		if strings.HasPrefix(s, prefix) {
			filtered = append(filtered, s)
		}
	}

	return filtered
}

func main() {
	fmt.Println(FilterByPrefix([]string{}, "a"))
	fmt.Println(FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a"))
}

// Output:
// []
// [abc array]
/*

Problem:

Given a list of integers and a target sum, find all unique combinations of two numbers in the list that sum up to the target sum.

E.g.
Input: [2, 7, 11, 15], target = 9
Output: [[2, 7], [7, 2], [11]]

