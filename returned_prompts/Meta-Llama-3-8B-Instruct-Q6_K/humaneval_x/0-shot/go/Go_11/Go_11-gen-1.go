Here is a simple Go function that performs a binary XOR operation on two input strings and returns the result as a string:

```go
func StringXor(a string, b string) string {
    result := ""
    for i := 0; i < len(a); i++ {
        bitA := a[i] - '0'
        bitB := b[i] - '0'
        result += fmt.Sprint(bitA ^ bitB)
    }
    return result
}
```

This function iterates over the characters of the input strings, converts each character to an integer (by subtracting the ASCII value of '0'), performs a bitwise XOR operation on the two integers, and appends the result as a string to the result variable. The final result is returned as a string. 

Note that this function assumes that the input strings have the same length. If the input strings have different lengths, you may want to pad the shorter string with leading zeros to match the length of the longer string. 

Also, this function returns the result as a string, but if you need the result as an integer or a byte slice, you can modify the function accordingly. 

Here is an example of how you can use this function:

```go
func main() {
    fmt.Println(StringXor("010", "110"))  // Output: "100"
}
```  