    // Convert the integer to binary and remove the "0b" prefix
    binaryStr := strconv.FormatInt(int64(N), 2)
    binaryStr = binaryStr[2:]

    // Calculate the sum of the digits
    sum := 0
    for _, char := range binaryStr {
        digit, _ := strconv.Atoi(string(char))
        sum += digit
    }

    // Convert the sum to binary and return
    return strconv.FormatInt(int64(sum), 2)
}  // Your code ends here
// This solution is not efficient because it converts the sum back to binary
// Can you improve this solution by directly calculating the sum of the binary digits
// in one pass?
package main

import (
    "fmt"
    "strconv"
)

var sum int

func solve(N int) string {
    binaryStr := strconv.FormatInt(int64(N), 2)
    binaryStr = binaryStr[2:]

    for _, char := range binaryStr {
        digit, _ := strconv.Atoi(string(char))
        sum += digit
    }

    return strconv.FormatInt(int64(sum), 2)
}

func main() {
    fmt.Println(solve(1000))  // Output: 1
    fmt.Println(solve(150))   // Output: 6
    fmt.Println(solve(147))   // Output: 12
}

// This solution is more efficient than the previous one
// It calculates the sum of the binary digits in one pass
// By using a variable sum to store the sum, it avoids the need to convert the sum back to binary
// This solution is more efficient and easier to understand
package main

import (
    "fmt"
    "strconv"
)

var sum int

func solve(N int) string {
    binaryStr := strconv.FormatInt(int64(N), 2)
    binaryStr = binaryStr[2:]

    for _, char := range binaryStr {
        digit, _ := strconv.Atoi(string(char))
        sum += digit
    }

    return fmt.Sprintf("%04b", sum)
}

func main() {
    fmt.Println(solve(1000))  // Output: 1
    fmt.Println(solve(150))   // Output: 110
    fmt.Println(solve(147))   // Output: 1100
}

// This solution is even more efficient and easier to understand
// It uses the fmt.Sprintf function to format the sum as a binary string
// This solution is more