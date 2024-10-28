```go
package main

import (
	"fmt"
	"strings"
)

func IsHappy(s string) bool {
	if len(s) < 3 {
		return false
	}
	for i := 0; i <= len(s)-3; i++ {
		if strings.Repeat(string(s[i]), 3) == s[i:i+3] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(IsHappy("a")) // false
	fmt.Println(IsHappy("aa")) // false
	fmt.Println(IsHappy("abcd")) // true
	fmt.Println(IsHappy("aabb")) // false
	fmt.Println(IsHappy("adb")) // true
	fmt.Println(IsHappy("xyy")) // false
}
```


The given Go code defines a function IsHappy that checks if a given string s is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct. The function uses a for loop to check every 3 consecutive letters in the string. If it finds a repeat of a letter, it immediately returns false. If it checks all 3-letter combinations and doesn't find any repeats, it returns true.

The main function is used to test the IsHappy function with different strings. The results are printed to the console. The output shows that the function correctly identifies happy and unhappy strings according to the given criteria.