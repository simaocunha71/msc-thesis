import (
    "fmt"
)

// Input are two strings a and b consisting only of 1s and 0s.
// Perform binary XOR on these inputs and return result also as a string.
// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {
    fmt.Println("StringXor:", a, b)
    lenA := len(a)
    lenB := len(b)
    for i := 0; i < lenA - 1 && i < lenB - 1; i++ {
        if a[i] == '0' && b[i] == '1' {
            a = "1" + a
            b = "0" + b
        } else if a[i] == '0' && b[i] == '0' {
            a = "0" + a
            b = "1" + b
        }
    }
    return fmt.Sprintf("%s%s", a, b)
}