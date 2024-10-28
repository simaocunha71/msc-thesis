
// Your code goes here

}

*/

package main

import "fmt"

func IsHappy(s string) bool {
	if len(s) < 3 {
		return false
	}
	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(IsHappy("a"))       // false
	fmt.Println(IsHappy("aa"))      // false
	fmt.Println(IsHappy("abcd"))    // true
	fmt.Println(IsHappy("aabb"))    // false
	fmt.Println(IsHappy("adb"))     // true
	fmt.Println(IsHappy("xyy"))     // false
	fmt.Println(IsHappy("aabca"))   // false
	fmt.Println(IsHappy("xyzzyx"))  // false
	fmt.Println(IsHappy("abcdefg")) // true
}
package main

import (
	"fmt"
	"regexp"
)

func main() {
	str := "Hello, my name is John. I love programming!"
	regex := regexp.MustCompile("[A-Z]")

	loc := regex.FindStringIndex(str)

	fmt.Println(loc)
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, my name is John. I love programming!"
	str = strings.ToLower(str)
	count := make(map[string]int)
	for _, char := range str {
		count[string(char)]++
	}

	fmt.Println(count)
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, my name is John. I love programming!"
	words :=