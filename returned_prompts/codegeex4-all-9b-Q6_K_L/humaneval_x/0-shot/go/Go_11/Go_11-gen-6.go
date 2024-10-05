import (
	"fmt"
	"unicode"
)

// Input are two strings a and b consisting only of 1s and 0s.
// Perform binary XOR on these inputs and return result also as a string.
// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {
	if len(a) != len(b) {
		return ""
	}
	result := ""
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			result += "1"
		} else {
			result += "0"
		}
	}
	return result
}

func main() {
	fmt.Println(StringXor("010", "110")) // Output: '100'
}

