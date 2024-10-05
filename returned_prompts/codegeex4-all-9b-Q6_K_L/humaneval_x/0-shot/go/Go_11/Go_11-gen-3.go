func StringXor(a string, b string) string {
    if len(a) != len(b) {
        panic("Strings are not the same length")
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

// Example usage:
fmt.Println(StringXor("010", "110")) // Output: "100"