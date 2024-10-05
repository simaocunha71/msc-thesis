    count := 0
    primeHexDigits := []rune{'2', '3', '5', '7', 'B', 'D'}
    for _, c := range num {
        for _, p := range primeHexDigits {
            if c == p {
                count++
                break
            }
        }
    }
    return count
}