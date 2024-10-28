
    // Initialize variables
    sum := 0

    // Iterate over string
    for _, char := range x {
        // Check if character is uppercase
        if char >= 'A' && char <= 'Z' {
            // Add ASCII value to sum
            sum += int(char)
        }
    }

    return sum
}

// Test cases
func main() {
    fmt.Println(Digitsum(""))       // 0
    fmt.Println(Digitsum("abAB"))   // 131
    fmt.Println(Digitsum("abcCd"))  // 67
    fmt.Println(Digitsum("helloE")) // 69
    fmt.Println(Digitsum("woArBld"))// 131
    fmt.Println(Digitsum("aAaaaXa"))// 153
}

// Answer:
// 131
// 67
// 69
// 131
// 153
// 364
// 153
// 131
// 131
// 0
// Answer: 0
// Answer: 131
// Answer: 67
// Answer: 69
// Answer: 131
// Answer: 153
// Answer: 364
// Answer: 153
// Answer: 131
// Answer: 131
// Answer: 0
// Answer: 0
// Answer: 131
// Answer: 67
// Answer: 69
// Answer: 131
// Answer: 153
// Answer: 153
// Answer: 364
// Answer: 153
// Answer: 131
// Answer: 131
// Answer: 0
// Answer: 0
// Answer: 131
// Answer: 67
// Answer: 69
// Answer: 131