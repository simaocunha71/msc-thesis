    primeDigits := []string{"2", "3", "5", "7", "B", "D"}
    count := 0
    for _, digit := range num {
        for _, primeDigit := range primeDigits {
            if string(digit) == primeDigit {
                count++
                break
            }
        }
    }
    return count
}


