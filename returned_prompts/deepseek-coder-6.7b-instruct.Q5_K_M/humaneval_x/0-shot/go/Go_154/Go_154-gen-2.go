
// Your code here

}

*/

package main

import (
	"fmt"
	"strings"
)

func CycpatternCheck(a, b string) bool {
	if len(b) > len(a) {
		return false
	}

	for i := 0; i < len(b); i++ {
		if strings.Contains(a, b) {
			return true
		}
		b = b[len(b)-1:] + b[:len(b)-1]
	}

	return false
}

func main() {
	fmt.Println(CycpatternCheck("abcd", "abd"))      // false
	fmt.Println(CycpatternCheck("hello", "ell"))     // true
	fmt.Println(CycpatternCheck("whassup", "psus"))  // false
	fmt.Println(CycpatternCheck("abab", "baa"))      // true
	fmt.Println(CycpatternCheck("efef", "eeff"))     // false
	fmt.Println(CycpatternCheck("himenss", "simen")) // true
}
package main

import (
	"fmt"
	"strings"
)

/*

