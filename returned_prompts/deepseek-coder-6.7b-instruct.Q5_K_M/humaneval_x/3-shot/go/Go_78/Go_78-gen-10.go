    primeDigits := map[rune]bool {
        '2': true,
        '3': true,
        '5': true,
        '7': true,
        'B': true,
        'D': true,
    }
    count := 0
    for _, digit := range num {
        if primeDigits[digit] {
            count++
        }
    }
    return count
}



