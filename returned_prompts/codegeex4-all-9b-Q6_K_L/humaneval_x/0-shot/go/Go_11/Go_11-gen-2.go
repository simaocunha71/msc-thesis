func StringXor(a string, b string) string {
    if len(a) != len(b) {
        panic("Input strings must be of equal length")
    }
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

// Example usage
fmt.Println(StringXor("010", "110")) // Output: "100"

B:
func StringXor(a string, b string) string {
    if len(a) != len(b) {
        panic("Input strings must be of equal length")
    }
    result := make([]byte, len(a))
    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result[i] = '0'
        } else {
            result[i] = '1'
        }
    }
    return string(result)
}

// Example usage
fmt.Println(StringXor("010", "110")) // Output: "100"

C:
func StringXor(a string, b string) string {
    if len(a) != len(b) {
        panic("Input strings must be of equal length")
    }
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

// Example usage
fmt.Println(StringXor("010", "110")) // Output: "100"

D:
func StringXor(a string, b string) string {
    if len(a) != len(b) {
        panic("Input strings must be of equal length")
    }
    result := make([]byte, len(a))
    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result[i] = '0'
        } else {
            result[i] = '1'
        }
    }
    return string(result)
}

// Example usage
fmt.Println(StringXor("010", "110")) // Output: "100"
