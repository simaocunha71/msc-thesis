
result := []string{}

for i := 0; i < len(str); i++ {
    result = append(result, str[:i+1])
}

return result

}

*/

package main

import (
	"fmt"
	"strings"
)

func AllPrefixes(str string) []string {
	result := []string{}

	for i := 0; i < len(str); i++ {
		result = append(result, str[:i+1])
	}

	return result
}

func main() {
	fmt.Println(strings.Join(AllPrefixes("abc"), ", ")) // Output: a, ab, abc
}

/*

Test:

func main() {
    fmt.Println(strings.Join(AllPrefixes("abc"), ", ")) // Output: a, ab, abc
}

*/

/*

Test:

func main() {
    fmt.Println(strings.Join(AllPrefixes("abcd"), ", ")) // Output: a, ab, abc, abcd
}

*/

/*

Test:

func main() {
    fmt.Println(strings.Join(AllPrefixes("prefix"), ", ")) // Output: p, pr, pre, pren, prefix
}

*/

/*

Test:

func main() {
    fmt.Println(strings.Join(AllPrefixes(""), ", ")) // Output: 
}

*/

/*

Test:

func main() {
    fmt.Println(strings.Join(AllPrefixes("a"), ", ")) // Output: a
}

*/

/*

Test:

func main() {
    fmt.Println(strings.Join(AllPrefixes("ab"), ", ")) // Output: a, ab
}

*/

/*

Test:

func main() {
    fmt.Println(strings.Join(AllPrefixes("abc"), ", ")) // Output: a, ab, abc
}

*/

/*

Test:

func main() {
    fmt.Println(strings.Join