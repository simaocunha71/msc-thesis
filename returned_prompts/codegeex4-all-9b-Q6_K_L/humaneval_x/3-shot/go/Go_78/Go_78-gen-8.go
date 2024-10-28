    primes := map[string]bool{
        "2": true,
        "3": true,
        "5": true,
        "7": true,
        "B": true,
        "D": true,
    }

    var count int = 0
    for _, c := range num {
        if primes[string(c)] {
            count += 1
        }
    }
    return count
}