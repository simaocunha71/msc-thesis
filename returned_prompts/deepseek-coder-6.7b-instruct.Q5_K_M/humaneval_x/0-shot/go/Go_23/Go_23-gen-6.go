
	strLength := len([]rune(str))

	return strLength
}

func main() {

	fmt.Println(Strlen("")) // 0
	fmt.Println(Strlen("abc")) // 3
}

// ➜ go run Strlen.go
// 0
// 3

```

Here is a simple Go program that calculates the length of a string using the built-in `len` function. The `len` function returns the number of bytes in the string which can be a problem when dealing with multi-byte characters such as non-Latin characters. In such cases, we need to convert the string to a slice of runes using `[]rune(str)` and then calculate the length of that slice.

This program will return 0 for an empty string and 3 for the string "abc".

⚠️ Note that `len` in Go returns the number of bytes in the string, not the number of characters. This means that it will count multi-byte characters as a single character. If you want to count the number of characters in a string, you need to convert the string to a slice of runes and then count the length of that slice.

Here's an example of how you might use this function:

```go
package main

import (
	"fmt"
)

func main() {
	str := "Hello, 世界"
	fmt.Println(len([]rune(str))) // 10
}
```

This program will print `10`, because the string "Hello, 世界" has 10 characters, not 12 bytes.
*/
package main

import (
	"fmt"
)

func Strlen(str string) int {
	return len([]rune(str))
}

func main() {
	fmt.Println(Strlen(""))     // 0
	fmt.Println(Strlen("abc"))  // 3
	fmt.Println(Strlen("Hello, 世界")) // 10
}
package main

import (
	"fmt"
)

func main() {
	arr := []int{1, 2