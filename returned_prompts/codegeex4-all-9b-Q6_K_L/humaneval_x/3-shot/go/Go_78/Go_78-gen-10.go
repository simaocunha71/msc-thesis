    primes := "2357BD"
    count := 0
    for _, c := range num {
        if string(c) == primes {
            count += 1
        }
    }
    return count
}

