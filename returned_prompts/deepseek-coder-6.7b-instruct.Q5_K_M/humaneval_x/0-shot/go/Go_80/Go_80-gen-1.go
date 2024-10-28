
// 1. Check if the length of the string is less than 3.
//    If it is, return false.
if len(s) < 3 {
    return false
}

// 2. Iterate through the string.
for i := 0; i < len(s) - 2; i++ {
    // 3. Check if the 3 consecutive characters are distinct.
    //    If they are not, return false.
    if s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2] {
        return false
    }
}

// 4. If none of the 3 consecutive characters are the same, return true.
return true
}

*/

package main

import (
	"fmt"
)

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
	fmt.Println(IsHappy("adb"))
	fmt.Println(IsHappy("xyy"))
	fmt.Println(IsHappy("abcd"))
	fmt.Println(IsHappy("aabb"))
	fmt.Println(IsHappy("a"))
	fmt.Println(IsHappy("aa"))
}
package main

import (
	"fmt"
	"strings"
)

func CountWords(str string) int {
	words := strings.Fields(str)
	return len(words)
}

func main() {
	fmt.Println(CountWords("Hello, how are you?"))
	fmt.Println(CountWords("This is a sentence with seven words"))
}
package main

import (
	"fmt"
	"strings"
)

func CountWords(str string) int {
	words