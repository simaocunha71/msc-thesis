Here is the Go function that performs the encoding as described:
```go
func Encode(message string) string {
    result := ""
    for _, char := range message {
        if char >= 'a' && char <= 'z' {
            result += string(char + 2)
        } else if char >= 'A' && char <= 'Z' {
            result += string(char + 2)
        } else {
            result += string(char)
        }
    }
    return result
}
```
This function iterates over each character in the input message. If the character is a lowercase letter, it adds the character shifted 2 positions ahead in the alphabet to the result. If the character is an uppercase letter, it does the same. If the character is not a letter, it simply adds it to the result as is.

The unit tests you provided are a good way to verify the function's behavior:
```go
func main() {
    fmt.Println(Encode("test")) // Output: TGST
    fmt.Println(Encode("This is a message")) // Output: tHKS KS C MGSSCGG
}
```
These tests will help ensure that the function works correctly for different inputs. You can add more tests to cover additional scenarios.