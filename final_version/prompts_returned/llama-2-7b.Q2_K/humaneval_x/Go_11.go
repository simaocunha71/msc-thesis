import (
    "fmt"
)

// Input are two strings a and b consisting only of 1s and 0s.
// Perform binary XOR on these inputs and return result also as a string.
// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {
    if len(b) < 8 || len(a) < 8 {
        fmt.Println("Inputs are too short. At least 8 Bytes required for each input")
    } else {
        var res string
        for i := 0; i < len(a); i++ {
            c, d := a[i], b[len(b)-1-i]
            if c == '0' && d == '0' {
                res = res + "0"
            } else if c == '0' || c == '1' {
                res = res + string(c)
            } else {
                res = res + string(d)
            }
        }
    return res + b[len(b)-1:]
}
