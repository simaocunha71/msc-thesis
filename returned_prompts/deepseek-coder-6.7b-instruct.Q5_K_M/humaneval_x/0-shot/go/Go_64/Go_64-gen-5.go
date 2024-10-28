    var vowels []string = []string{"a", "e", "i", "o", "u"}
    var count int = 0
    s = strings.ToLower(s)
    for _, letter := range s {
        for _, vowel := range vowels {
            if string(letter) == vowel {
                count++
            }
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}

func main() {
    fmt.Println(VowelsCount("abcde")) // 2
    fmt.Println(VowelsCount("ACEDY")) // 3
}

*/

package main

import (
	"fmt"
	"strings"
)

// Write a function VowelsCount which takes a string representing
// a word as input and returns the number of vowels in the string.
// Vowels in this case are  'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
// vowel, but only when it is at the end of the given word.
// 
// Example:
// >>> VowelsCount("abcde")
// 2
// >>> VowelsCount("ACEDY")
// 3
func VowelsCount(s string) int {
	var vowels []string = []string{"a", "e", "i", "o", "u"}
	var count int = 0
	s = strings.ToLower(s)
	for _, letter := range s {
		for _, vowel := range vowels {
			if string(letter) == vowel {
				count++
			}
		}
	}
	if s[len(s)-1] == 'y' {
		count++
	}
	return count
}

func main() {
	fmt.Println(VowelsCount("abcde")) // 2
	fmt.Println(VowelsCount("ACEDY")) // 3
}

```
































