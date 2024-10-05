
// Initialize a count variable to keep track of the number of occurrences.
count := 0

// Use the built-in Go function `strings.Contains` to check if the substring exists in the string.
// If it does, increment the count and use `strings.Replace` to remove the first instance of the substring from the string,
// then repeat the process until no instances of the substring are left.
for strings.Contains(str, substring) {
	count++
	str = strings.Replace(str, substring, "", 1)
}

// Return the final count.
return count
}


*/

package main

import (
	"fmt"
	"strings"
)

func HowManyTimes(str string, substring string) int {
	count := 0
	for strings.Contains(str, substring) {
		count++
		str = strings.Replace(str, substring, "", 1)
	}
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a"))        // 0
	fmt.Println(HowManyTimes("aaa", "a"))     // 3
	fmt.Println(HowManyTimes("aaaa", "aa"))   // 3
	fmt.Println(HowManyTimes("bananan", "na")) // 2
}
