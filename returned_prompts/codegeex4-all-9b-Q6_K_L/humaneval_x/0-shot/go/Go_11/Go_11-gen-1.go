import (
    "fmt"
)

// Input are two strings a and b consisting only of 1s and 0s.
// Perform binary XOR on these inputs and return result also as a string.
// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {
    if len(a) != len(b) {
        return ""
    }

    var result []byte
    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result = append(result, '0')
        } else {
            result = append(result, '1')
        }
    }

    return string(result)
}