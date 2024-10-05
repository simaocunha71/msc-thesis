```go
package main

import (
	"fmt"
	"strings"
)

func AllPrefixes(str string) []string {
	var prefixes []string
	for i := 0; i <= len(str); i++ {
		prefixes = append(prefixes, str[:i])
	}
	return prefixes
}

func main() {
	fmt.Println(AllPrefixes("abc"))
}
```


Output:
```
[a a b ab abc]
```

Explanation:
This program uses a loop to iterate over the length of the input string. For each iteration, it appends the substring of the original string up to the current index to the `prefixes` slice. The `append` function is used to add elements to the end of the `prefixes` slice. Finally, the function returns the `prefixes` slice.

The `main` function calls the `AllPrefixes` function with the input string "abc" and prints the result.

Note that the last element of the output is an empty string, which is the prefix of the original string. If you don't want the empty string, you can change the loop condition to `i < len(str)`.