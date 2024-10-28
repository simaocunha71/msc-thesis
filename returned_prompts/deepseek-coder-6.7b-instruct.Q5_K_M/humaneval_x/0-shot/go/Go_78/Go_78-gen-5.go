
// your code here

}

*/

package main

import (
	"fmt"
	"strings"
)

func HexKey(num string) int {
	primeHex := []string{"2", "3", "5", "7", "B", "D"}
	count := 0
	for _, v := range num {
		if strings.Contains(strings.Join(primeHex, ""), string(v)) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))
	fmt.Println(HexKey("1077E"))
	fmt.Println(HexKey("ABED1A33"))
	fmt.Println(HexKey("123456789ABCDEF0"))
	fmt.Println(HexKey("2020"))
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, how are you?"

	// convert the string to uppercase
	upperStr := strings.ToUpper(str)
	fmt.Println(upperStr) // prints: HELLO, HOW ARE YOU?

	// convert the string to lowercase
	lowerStr := strings.ToLower(str)
	fmt.Println(lowerStr) // prints: hello, how are you?

	// check if the string contains a substring
	containsStr := strings.Contains(str, "how")
	fmt.Println(containsStr) // prints: true

	// count the number of occurrences of a substring
	countStr := strings.Count(str, "o")
	fmt.Println(countStr) // prints: 2

	// replace all occurrences of a substring
	replaceStr := strings.ReplaceAll(str, "o", "a")
	fmt.Println(replaceStr) // prints: Hella, hara are yua?

	// split the string into a slice of substrings
	splitStr := strings.Split(str, " ")
	fmt.Println