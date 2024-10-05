    str = strings.ToLower(str)
    count := 0
    chars := make(map[rune]bool)

    for _, char := range str {
        if _, ok := chars[char]; !ok {
            chars[char] = true
            count++
        }
    }

    return count
}

*/

package main

import (
	"fmt"
	"strings"
)

func CountDistinctCharacters(str string) int {
	str = strings.ToLower(str)
	count := 0
	chars := make(map[rune]bool)

	for _, char := range str {
		if _, ok := chars[char]; !ok {
			chars[char] = true
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ")) // 3
	fmt.Println(CountDistinctCharacters("Jerry"))   // 4
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, world"
	str = strings.Replace(str, "world", "Go", 1) // Replace the first occurrence of "world" with "Go"
	fmt.Println(str)
}

/*
Output:
Hello, Go
*/
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, world"
	str = strings.ToUpper(str) // Convert the string to uppercase
	fmt.Println(str)
}

/*
Output:
HELLO, WORLD
*/
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, world"
	str = strings.TrimSpace(str) // Remove leading and trailing spaces
	fmt.Println(str)
}

/*
Output:
Hello, world
*/
package main

import (