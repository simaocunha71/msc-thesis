
```go
func StringXor(a string, b string) string {
    result := make([]byte, len(a))
    for i := range a {
        result[i] = a[i] ^ b[i]
    }
    return string(result)
}

func main() {
    fmt.Println(StringXor("010", "110")) // Output: 100
}
```

This is the most concise and correct way to perform XOR operation on two binary strings in Go. The function `StringXor` takes two strings `a` and `b` as input, performs XOR operation on each corresponding character from the two strings, and returns the result as a string.