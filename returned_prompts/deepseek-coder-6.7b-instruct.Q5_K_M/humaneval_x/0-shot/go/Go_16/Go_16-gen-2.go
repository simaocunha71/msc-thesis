    str = strings.ToLower(str)
    m := make(map[rune]int)
    for _, char := range str {
        m[char]++
    }
    return len(m)
}

func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ")) // Output: 3
    fmt.Println(CountDistinctCharacters("Jerry"))  // Output: 4
}

*/

import (
	"fmt"
	"strings"
)

func CountDistinctCharacters(str string) int {
	str = strings.ToLower(str)
	m := make(map[rune]int)
	for _, char := range str {
		m[char]++
	}
	return len(m)
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ")) // Output: 3
	fmt.Println(CountDistinctCharacters("Jerry"))  // Output: 4
}
package main

import (
	"fmt"
	"strings"
)

// CountDistinctCharacters is a function that counts the distinct characters in a string.
// It converts the string to lower case and uses a map to count the occurrence of each character.
// Finally, it returns the length of the map which represents the number of distinct characters.
func CountDistinctCharacters(str string) int {
	str = strings.ToLower(str)
	m := make(map[rune]int)
	for _, char := range str {
		m[char]++
	}
	return len(m)
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ")) // Output: 3
	fmt.Println(CountDistinctCharacters("Jerry"))  // Output: 4
}
package main

import (
	"testing"
)

func TestCountDistinctCharacters(t *testing.T) {
	tables := []struct {
		x string
		n int
	}{
		{"xyzXYZ", 3},
		{"Jerry", 4