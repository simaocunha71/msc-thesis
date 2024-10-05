```go
func StringXor(a string, b string) string {
    result := ""
    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}

func main() {
    fmt.Println(StringXor("010", "110")) // Output: 100
}
```

Explanation:
This function performs a binary XOR operation on the input strings `a` and `b`. It iterates through each character of the strings and checks if they are the same or not. If they are the same, it appends "0" to the result string. If they are not the same, it appends "1". The result is a string representing the binary XOR of the input strings.

In the `main` function, we call `StringXor` with the inputs "010" and "110" and print the result, which is "100". This is because the binary XOR of "010" and "110" is indeed "100".