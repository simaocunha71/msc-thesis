
func Concatenate(strings []string) string {
  result := ""

  for _, str := range strings {
    result += str
  }

  return result
}

*/

package main

import (
	"fmt"
)

func Concatenate(strings []string) string {
	result := ""

	for _, str := range strings {
		result += str
	}

	return result
}

func main() {
	fmt.Println(Concatenate([]string{}))
	fmt.Println(Concatenate([]string{"a", "b", "c"}))
}
package main

import (
	"fmt"
)

func main() {
	fmt.Println(IsPalindrome("racecar"))
	fmt.Println(IsPalindrome("hello"))
}

func IsPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

/*
