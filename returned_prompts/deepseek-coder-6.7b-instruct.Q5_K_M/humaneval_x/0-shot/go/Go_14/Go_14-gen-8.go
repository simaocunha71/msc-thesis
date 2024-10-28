
prefixes := make([]string, 0)
for i := 0; i < len(str); i++ {
	prefixes = append(prefixes, str[0:i+1])
}
return prefixes
}

*/

package main

import (
	"fmt"
	"strings"
)

func AllPrefixes(str string) []string {
	prefixes := make([]string, 0)
	for i := 0; i < len(str); i++ {
		prefixes = append(prefixes, str[0:i+1])
	}
	return prefixes
}

func main() {
	str := "abc"
	prefixes := AllPrefixes(str)
	fmt.Println(strings.Join(prefixes, ", "))
}

//Output: a, ab, abc


/*
In this code, we use a loop to iterate over each character of the string. We use the built-in `append` function to add the prefix (which is a substring of the input string from index 0 to the current index plus one) to the `prefixes` slice. Finally, we return the `prefixes` slice.

The `AllPrefixes` function returns a slice of all prefixes of the input string, from the shortest to the longest. The `main` function demonstrates how to use the `AllPrefixes` function by passing in the string "abc" and printing out the prefixes.
*/









































































































































































