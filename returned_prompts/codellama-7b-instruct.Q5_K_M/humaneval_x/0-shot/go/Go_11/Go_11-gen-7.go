import (
    "fmt"
)

// Input are two strings a and b consisting only of 1s and 0s.
// Perform binary XOR on these inputs and return result also as a string.
// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {
    var result string
    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}

fmt.Println(StringXor("1010", "1010")) // Output: 1000
fmt.Println(StringXor("0000", "0000")) // Output: 0000
fmt.Println(StringXor("0101", "0101")) // Output: 0000
fmt.Println(StringXor("1100", "1100")) // Output: 1000
fmt.Println(StringXor("1001", "1001")) // Output: 0000
fmt.Println(StringXor("1011", "1011")) // Output: 0000
fmt.Println(StringXor("1111", "1111")) // Output: 1000
fmt.Println(StringXor("1110", "1110")) // Output: 1000
fmt.Println(StringXor("1111", "1110")) // Output: 0001
fmt.Println(StringXor("1111", "1111")) // Output: 1000
fmt.Println(StringXor("1111", "1111")) // Output: 1000
fmt.Println(StringXor("1111", "1111")) // Output: 1000
fmt.Println(StringXor("111