import (
    "fmt"
)

// Input are two strings a and b consisting only of 1s and 0s.
// Perform binary XOR on these inputs and return result also as a string.
// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {
    var result string
    for i, j := 0, 0; i < len(a) || j < len(b); {
        if i < len(a) {
            result += string(a[i])
            i++
        }
        if j < len(b) {
            result += string(b[j])
            j++
        }
    }
    return result
}

