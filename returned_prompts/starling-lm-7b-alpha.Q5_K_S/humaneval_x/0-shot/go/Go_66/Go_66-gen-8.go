
```go
package main

import (
	"fmt"
	"unicode"
)

func Digitsum(x string) int {
	sum := 0
	for _, r := range x {
		if unicode.IsUpper(r) {
			sum += int(r)
		}
	}
	return sum
}

func main() {
	fmt.Println(Digitsum(""))       // 0
	fmt.Println(Digitsum("abAB"))   // 131
	fmt.Println(Digitsum("abcCd"))  // 67
	fmt.Println(Digitsum("helloE")) // 69
	fmt.Println(Digitsum("woArBld")) // 131
	fmt.Println(Digitsum("aAaaaXa")) // 153
}
```

Explanation:
The function `Digitsum` takes a string `x` as input and returns the sum of the ASCII codes of its upper characters only. It uses a for loop to iterate through each character in the string and the `unicode.IsUpper` function to check if the character is uppercase. If the character is uppercase, the ASCII code of the character is added to the sum. Finally, the function returns the sum.

The `main` function demonstrates the usage of the `Digitsum` function by passing different strings as arguments and printing the results.

The output of the program is:
```
0
131
67
69
131
153
```

This means that the sum of the ASCII codes of the upper characters in the respective strings are: 0, 131, 67, 69, 131, and 153.

The `Digitsum` function can be used to calculate the sum of the upper characters' ASCII codes in any given string.

Note: The ASCII codes for uppercase letters range from 65 to 90.

```go
package main

import (
	"fmt"
	"unicode"
)

func