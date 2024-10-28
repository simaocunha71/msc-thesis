    primeDigits := []string{"2", "3", "5", "7", "B", "D"}
    counter := 0
    for _, digit := range num {
        for _, primeDigit := range primeDigits {
            if string(digit) == primeDigit {
                counter++
            }
        }
    }
    return counter
}



