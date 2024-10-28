```go
func StringXor(a string, b string) string {
    result := ""
    for i := 0; i < len(a); i++ {
        if a[i] == '1' && b[i] == '1' || a[i] == '0' && b[i] == '0' {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}
```


The above code performs a binary XOR operation on two input strings. It iterates through each character in the strings and checks if they are both 1 or both 0. If they are, it appends a 0 to the result. If they are not, it appends a 1. The result is a new string representing the binary XOR operation.

For example, if we call `StringXor('010', '110')`, the function will return `'100'` as the result of the binary XOR operation on the two input strings.