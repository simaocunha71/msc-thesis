// Start by defining the set of prime hexadecimal digits
primeHexDigits := map[rune]bool{'2': true, '3': true, '5': true, '7': true, 'B': true, 'D': true}

// Initialize the count of prime hexadecimal digits
count := 0

// Iterate over the hexadecimal digits in the input string
for _, digit := range num {
    // Check if the digit is a prime hexadecimal digit
    if primeHexDigits[digit] {
        // If it is, increment the count
        count++
    }
}

// Return the count of prime hexadecimal digits
return count
}
