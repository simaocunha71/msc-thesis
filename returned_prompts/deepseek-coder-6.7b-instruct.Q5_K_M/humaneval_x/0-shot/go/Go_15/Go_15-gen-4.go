    var result string
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }

    return strings.TrimSpace(result)
}

*/

package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Return a string containing space-delimited numbers starting from 0 upto n inclusive.
// >>> StringSequence(0)
// 0
// >>> StringSequence(5)
// 0 1 2 3 4 5
func StringSequence(n int) string {
	var result string
	for i := 0; i <= n; i++ {
		result += strconv.Itoa(i) + " "
	}
	return strings.TrimSpace(result)
}

func main() {
	fmt.Println(StringSequence(0))
	fmt.Println(StringSequence(5))
}
package main

import (
	"fmt"
	"strings"
)

// CountVowels counts the number of vowels in a given string.
// 
// For example,
// 
// 	CountVowels("hello") returns 2
// 	CountVowels("world") returns 1
// 	CountVowels("scala") returns 2
// 	CountVowels("java") returns 2
func CountVowels(s string) int {
	vowels := "aeiou"
	count := 0
	for _, c := range strings.ToLower(s) {
		if strings.ContainsRune(vowels, c) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(CountVowels("hello")) // 2
	fmt.Println(CountVowels("world")) // 1
	fmt.Println(CountVowels("scala")) // 2
	fmt.Println(CountVowels("java"))  // 2
}
package main

import (
	"fmt"
)

// ReverseString returns