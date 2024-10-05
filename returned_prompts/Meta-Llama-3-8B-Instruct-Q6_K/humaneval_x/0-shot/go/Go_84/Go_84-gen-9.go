    // Convert the number N to binary and store it in a variable
    binary := strconv.FormatInt(int64(N), 2)
    // Initialize a variable to store the sum of digits
    sum := 0
    // Iterate over the binary string
    for _, char := range binary {
        // Convert the character to an integer
        digit, _ := strconv.Atoi(string(char))
        // Add the digit to the sum
        sum += digit
    }
    // Convert the sum to a binary string
    binarySum := strconv.FormatInt(int64(sum), 2)
    // Return the binarySum
    return binarySum

} 
