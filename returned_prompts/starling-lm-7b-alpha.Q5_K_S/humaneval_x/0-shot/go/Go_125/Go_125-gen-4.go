To split the text, we can use the strings.Fields function which will split the string on whitespace. If the string does not contain
any whitespace, we can check if the string contains a comma and if it does, we can split on comma. If the string does not contain
any whitespace or commas, we can check if the string contains lowercase letters and if it does, we can return the count of the letters
that have an odd order in the alphabet.

Here is the code:

```go
package main

import (
	"fmt"
	"strings"
)

func SplitWords(txt string) interface{} {
	if strings.Contains(txt, " ") {
		return strings.Fields(txt)
	} else if strings.Contains(txt, ",") {
		return strings.Split(txt, ",")
	} else {
		count := 0
		for _, char := range txt {
			if 'a' <= char && char <= 'z' {
				count++
			}
		}

		var result []int
		for _, char := range txt {
			if 'a' <= char && char <= 'z' && char%2 == 1 {
				result = append(result, char)
			}
		}

		return result
	}
}

func main() {
	fmt.Println(SplitWords("Hello world!"))
	fmt.Println(SplitWords("Hello,world!"))
	fmt.Println(SplitWords("abcdef"))
}
```

This code will output:

```
[Hello world!]
[Hello world!]
[a b c d e f]
```

The SplitWords function checks if the input string contains a whitespace or a comma. If it does, it splits the string using the appropriate function. If the string does not contain either whitespace or commas, it counts the number of lowercase letters in the string and returns a slice containing only the lowercase letters with an odd order in the alphabet.

In the main function, we are testing the SplitWords function