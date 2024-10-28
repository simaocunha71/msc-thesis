    primes := "2357BD"

    count := 0
    for _, c := range num {
        if strings.Contains(primes, string(c)) {
            count += 1
        }
    }

    return count
}



