    primes := []rune{'2', '3', '5', '7', 'B', 'D', 'F'}
    count := 0
    for _, c := range num {
        if contains(primes, c) {
            count++
        }
    }
    return count
}

func contains(arr []rune, target rune) bool {
    for _, v := range arr {
        if v == target {
            return true
        }
    }
    return false
}