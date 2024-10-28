// 1.1
// I would start by creating a list of the prime hexadecimal digits
// and a map of the hexadecimal digits to their decimal values
// to use when comparing the hex digits to the prime list
    primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    hexMap := map[rune]int{
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

// 1.2
// Then I would loop through the digits in the hex number
// and check if the decimal value of each digit is in the list of primes
    primeCount := 0
    for _, digit := range num {
        if _, ok := hexMap[digit]; ok {
            if contains(primes, hexMap[digit]) {
                primeCount++
            }
        }
    }

// 1.3
// Finally, I would return the count of prime digits
    return primeCount
}

// 1.4
// Helper function to check if a slice contains a given value
func contains(slice []int, value int) bool {
    for _, v := range slice {
        if v == value {
            return true
        }
    }
    return false
}

