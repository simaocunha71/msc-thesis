
// Write your code here

}

*/

package main

import (
	"strings"
)

func CycpatternCheck(a, b string) bool {

	for i := 0; i < len(b); i++ {
		if strings.Contains(a, b) {
			return true
		}
		b = b[len(b)-1:] + b[:len(b)-1]
	}
	return false
}

func main() {
	println(CycpatternCheck("abcd", "abd")) // false
	println(CycpatternCheck("hello", "ell")) // true
	println(CycpatternCheck("whassup", "psus")) // false
	println(CycpatternCheck("abab", "baa")) // true
	println(CycpatternCheck("efef", "eeff")) // false
	println(CycpatternCheck("himenss", "simen")) // true
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello World"
	fmt.Printf("Original String: %s\n", str)

	str = strings.Replace(str, "World", "Gophers", -1)

	fmt.Printf("Modified String: %s\n", str)
}

// Output:
// Original String: Hello World
// Modified String: Hello Gophers
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, World"

	substr := "World"
	index := strings.Index(str, substr)

	fmt.Printf("Substring '%s' found at index: %d\n", substr, index)
}

// Output:
// Substring 'World' found at index: 7
package main

import "fmt"

func main() {
	var a int = 10
	var b int = 20

	swap(&a, &b)

	fmt.Printf("a = %d, b = %d\