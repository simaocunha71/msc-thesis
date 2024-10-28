    primes := make([]bool, 100)
    for i := 2; i < 100; i++ {
        for j := 2; j < i; j++ {
            if i % j == 0 {
                primes[i] = false
                break
            }
            if j == i - 1 {
                primes[i] = true
            }
        }
    }

    for i := 2; i < a; i++ {
        if primes[i] == false {
            continue
        }
        for j := i + 1; j < a; j++ {
            if primes[j] == false {
                continue
            }
            for k := j + 1; k < a; k++ {
                if primes[k] == false {
                    continue
                }
                if i * j * k == a {
                    return true
                }
            }
        }
    }
    return false
}












































































































































































































































































