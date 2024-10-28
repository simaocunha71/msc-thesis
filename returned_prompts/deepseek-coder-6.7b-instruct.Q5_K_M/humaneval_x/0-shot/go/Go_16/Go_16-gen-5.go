    count := 0
    distinct := make(map[rune]bool)

    for _, letter := range strings.ToLower(str){
        if _, ok := distinct[letter]; !ok {
            distinct[letter] = true
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ")) // 3
    fmt.Println(CountDistinctCharacters("Jerry"))  // 4
}

*/

package main

import (
	"fmt"
	"strings"
)

func CountDistinctCharacters(str string) int {
	count := 0
	distinct := make(map[rune]bool)

	for _, letter := range strings.ToLower(str) {
		if _, ok := distinct[letter]; !ok {
			distinct[letter] = true
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ")) // 3
	fmt.Println(CountDistinctCharacters("Jerry"))  // 4
}
package main

import (
	"fmt"
	"strings"
)

// Given a string, return a string where each character occurs only once. The given string may include spaces and punctuation.
// 
// 
// 