Here is a simple and efficient solution in Go:

```go
func StringXor(a string, b string) string {
    result := ""
    for i := 0; i < len(a); i++ {
        if string(a[i]) == string(b[i]) {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}
```

This function iterates over the input strings character by character. If the characters at the same position are the same, it appends "0" to the result string. Otherwise, it appends "1". The result is a string representing the binary XOR operation on the input strings. 

For example, if you call `StringXor("010", "110")`, it will return "100", which is the correct result of the binary XOR operation on the input strings.