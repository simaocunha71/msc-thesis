    primes := map[byte]bool{
        '2': true,
        '3': true,
        '5': true,
        '7': true,
        'B': true,
        'D': true,
    }
    count := 0
    for _, c := range num {
        if primes[byte(c)] {
            count++
        }
    }
    return count
}



