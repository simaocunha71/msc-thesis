```go
func StringXor(a string, b string) string {
    result := ""
    for i := 0; i < len(a); i++ {
        if a[i] == '0' && b[i] == '0' {
            result += "0"
        } else if a[i] == '1' && b[i] == '1' {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}
```

Explanation:
The function `StringXor` takes two strings `a` and `b` as input. It iterates over each character in the strings, performs a binary XOR operation, and appends the result to a new string. The binary XOR operation is implemented using a simple if-else statement. If both characters are '0', the result is '0'. If both characters are '1', the result is '0'. Otherwise, the result is '1'. The final result is returned as a string.

Example:
```go
fmt.Println(StringXor("010", "110")) // Output: "100"
```


Bugs:
1. The function does not handle the case where the input strings are of different lengths. It will panic if the input strings are of different lengths.
2. The function does not handle the case where the input strings contain characters other than '0' and '1'. It will panic if the input strings contain characters other than '0' and '1'.

Solution:
To fix the bugs, we need to add error handling to the function. Here is a revised version of the function:

```go
func StringXor(a string, b string) (string, error) {
    if len(a) != len(b) {
        return "", errors.New("input strings must be of the same length")
    }
    result := ""
    for i := 0; i < len(a); i++ {
        if a[i] != '0' && a[i] != '1' {
            return "", errors.New("input strings must contain only '0' and '1'")
        }
        if b[i] != '0' && b[i] != '1' {
            return "", errors.New("input strings must contain only '0' and '1'")
        }
        if a[i] == '0' && b[i] == '0' {
            result += "0"
        } else if a[i] == '1' &&