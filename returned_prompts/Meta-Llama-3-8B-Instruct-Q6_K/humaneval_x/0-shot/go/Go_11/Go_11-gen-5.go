```go
func StringXor(a string, b string) string {
    result := ""
    for i, j := 0, 0; i < len(a) && j < len(b); i, j = i+1, j+1 {
        if a[i] == '1' && b[j] == '1' {
            result += '0'
        } else if a[i] == '0' && b[j] == '0' {
            result += '0'
        } else {
            result += '1'
        }
    }
    for i := i; i < len(a); i++ {
        if a[i] == '1' {
            result += '1'
        } else {
            result += '0'
        }
    }
    for j := j; j < len(b); j++ {
        if b[j] == '1' {
            result += '1'
        } else {
            result += '0'
        }
    }
    return result
}
```


Explanation:

*   We iterate through both strings `a` and `b` simultaneously using two pointers `i` and `j`. We check the bits at the current positions of both strings and perform the XOR operation accordingly.
*   If both bits are 1, we append 0 to the result string.
*   If both bits are 0, we append 0 to the result string.
*   If one bit is 1 and the other is 0, we append 1 to the result string.
*   After the loop, we handle any remaining bits in either string by iterating through the remaining portion of the string and appending the corresponding bits to the result string.
*   Finally, we return the result string.