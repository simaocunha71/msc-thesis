import (
    "fmt"
)

// Input are two strings a and b consisting only of 1s and 0s.
// Perform binary XOR on these inputs and return result also as a string.
// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {
    return fmt.Sprintf("%b", (int(a[0] - '0') ^ int(b[0] - '0')))
}

func main() {
    fmt.Println(StringXor("010", "110"))
}
