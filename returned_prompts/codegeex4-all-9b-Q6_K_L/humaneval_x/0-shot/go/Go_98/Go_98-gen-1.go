You can solve this problem by iterating over the string, checking each character to see if it is an uppercase vowel ('A', 'E', 'I', 'O', 'U') and if its index is even. Here is an example implementation in Go:

```go
package main

import (
	"strings"
)

func CountUpper(s string) int {
	count := 0
	for i, c := range s {
		if i%2 == 0 && strings.ContainsRune("AEIOU", c) {
			count++
		}
	}
	return count
}

func main() {
	println(CountUpper("aBCdEf")) // 1
	println(CountUpper("abcdefg")) // 0
	println(CountUpper("dBBE")) // 0
}
```

In this code, we use a `for` loop to iterate over each character in the string. We use the `range` keyword to get both the index and the character at that index. We then check if the index is even (`i%2 == 0`) and if the character is one of the uppercase vowels ('A', 'E', 'I', 'O', 'U'). If both conditions are true, we increment the `count` variable. Finally, we return the `count` variable, which represents the number of uppercase vowels at even indices in the string.