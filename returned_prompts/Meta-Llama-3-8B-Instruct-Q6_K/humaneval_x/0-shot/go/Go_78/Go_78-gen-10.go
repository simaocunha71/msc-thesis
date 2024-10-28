// Create a set of prime numbers in hexadecimal
// 2, 3, 5, 7, B, D, F
primeHex := map[rune]bool{'2': true, '3': true, '5': true, '7': true, 'B': true, 'D': true, 'F': true}

// Initialize the count of prime digits
count := 0

// Iterate over the hexadecimal number
for _, rune := range num {
    // Check if the hexadecimal digit is a prime number
    if _, ok := primeHex[rune]; ok {
        // If it is a prime number, increment the count
        count++
    }
}

// Return the count of prime digits
return count
}  



